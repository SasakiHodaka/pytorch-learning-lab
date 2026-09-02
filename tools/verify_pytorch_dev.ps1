[CmdletBinding()]
param(
    [string]$PyTorchRoot = (Join-Path $PSScriptRoot "..\..\pytorch-dev")
)

$ErrorActionPreference = "Stop"

$PyTorchRoot = (Resolve-Path $PyTorchRoot).Path
$Python = Join-Path $PyTorchRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    throw "Python virtual environment not found: $Python"
}

Push-Location $PyTorchRoot
try {
    & $Python -c @'
import torch

print(f"torch version: {torch.__version__}")
print(f"torch location: {torch.__file__}")
print(f"CUDA available: {torch.cuda.is_available()}")
result = (torch.tensor([1.0, 2.0]) * 2).tolist()
assert result == [2.0, 4.0]
print(f"CPU tensor smoke test: {result}")
'@
    if ($LASTEXITCODE -ne 0) {
        throw "PyTorch verification failed with exit code $LASTEXITCODE"
    }
}
finally {
    Pop-Location
}
