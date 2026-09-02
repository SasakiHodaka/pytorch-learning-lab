param(
    [ValidateRange(1, 100)]
    [int]$MaxIssues = 25,
    [string]$Repository = "pytorch/pytorch"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI (gh) is required."
}

gh auth status 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Authenticate GitHub CLI with 'gh auth login' first."
}

$query = "repo:$Repository is:issue is:open label:actionable"
$issuesJson = gh api --method GET search/issues `
    -f "q=$query" `
    -f sort=created `
    -f order=desc `
    -f "per_page=$MaxIssues"

if ($LASTEXITCODE -ne 0) {
    throw "Failed to query actionable issues."
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
