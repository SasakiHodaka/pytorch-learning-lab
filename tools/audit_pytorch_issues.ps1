param(
    [ValidateRange(1, 100)]
    [int]$MaxIssues = 25,
    [string]$Repository = "pytorch/pytorch",
    [ValidateNotNullOrEmpty()]
    [string]$Label = "actionable"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI (gh) is required."
}

cmd /c "gh auth status >nul 2>nul"
if ($LASTEXITCODE -ne 0) {
    throw "Authenticate GitHub CLI with 'gh auth login' first."
}

$query = "repo:$Repository is:issue is:open label:`"$Label`""
$encodedQuery = [Uri]::EscapeDataString($query)
$searchEndpoint = "search/issues?q=$encodedQuery&sort=created&order=desc&per_page=$MaxIssues"
$issuesJson = gh api --method GET $searchEndpoint

if ($LASTEXITCODE -ne 0) {
    throw "Failed to query issues labeled '$Label'."
}

$issues = ($issuesJson | ConvertFrom-Json).items
$results = foreach ($issue in $issues) {
    $timelineJson = gh api `
        -H "Accept: application/vnd.github+json" `
        "repos/$Repository/issues/$($issue.number)/timeline?per_page=100"

    if ($LASTEXITCODE -ne 0) {
        throw "Failed to query timeline for issue #$($issue.number)."
    }

    $timeline = $timelineJson | ConvertFrom-Json
    $openPullRequests = @(
        $timeline |
            Where-Object {
                $_.event -eq "cross-referenced" -and
                $_.source.issue.pull_request -and
                $_.source.issue.state -eq "open"
            } |
            ForEach-Object { $_.source.issue.number } |
            Sort-Object -Unique
    )

    [PSCustomObject]@{
        Number = $issue.number
        OpenPullRequests = $openPullRequests -join ","
        Comments = $issue.comments
        Updated = $issue.updated_at
        Title = $issue.title
        Url = $issue.html_url
    }
}

$results | Sort-Object Number -Descending
