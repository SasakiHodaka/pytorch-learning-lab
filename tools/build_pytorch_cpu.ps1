[CmdletBinding()]
param(
    [string]$PyTorchRoot,
    [ValidateRange(1, 8)]
    [int]$Jobs = 2
)

$ErrorActionPreference = "Stop"

if (-not $PyTorchRoot) {
    $PyTorchRoot = Join-Path $PSScriptRoot "..\..\pytorch-dev"
}

$PyTorchRoot = (Resolve-Path $PyTorchRoot).Path
$Python = Join-Path $PyTorchRoot ".venv\Scripts\python.exe"
$VcVars = "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

if (-not (Test-Path $Python)) {
    throw "Python virtual environment not found: $Python"
}

if (-not (Test-Path $VcVars)) {
    throw "Visual C++ environment script not found: $VcVars"
}

# Launch-VsDevShell can fail on localized Visual Studio metadata. Import the
# environment emitted by vcvars64.bat instead.
$environmentLines = cmd.exe /d /s /c ('"{0}" >nul && set' -f $VcVars)
foreach ($line in $environmentLines) {
    if ($line -match '^([^=]+)=(.*)$') {
        Set-Item -Path ("Env:{0}" -f $Matches[1]) -Value $Matches[2]
    }
}

$env:USE_CUDA = "0"
$env:USE_XPU = "0"
$env:USE_DISTRIBUTED = "0"
$env:USE_FLASH_ATTENTION = "0"
$env:USE_MEM_EFF_ATTENTION = "0"
$env:USE_KINETO = "0"
$env:USE_FBGEMM = "0"
$env:USE_NNPACK = "0"
$env:USE_XNNPACK = "0"
$env:USE_MKLDNN = "0"
$env:BUILD_TEST = "0"
$env:MAX_JOBS = $Jobs.ToString()
$env:CMAKE_PREFIX_PATH = Join-Path $PyTorchRoot ".venv"

Push-Location $PyTorchRoot
try {
    & $Python -m pip install --no-build-isolation -v -e .
    if ($LASTEXITCODE -ne 0) {
        throw "PyTorch build failed with exit code $LASTEXITCODE"
    }
}
finally {
    Pop-Location
}
