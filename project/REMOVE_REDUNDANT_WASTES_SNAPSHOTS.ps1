#Requires -Version 5.1
<#
.SYNOPSIS
  Remove only the 34 owner-approved Wastes administrative duplicates.
.DESCRIPTION
  Defaults to preview. -Apply deletes only after all 42 SHA-256 values,
  file sizes, Git state, and the pinned main revision pass verification.
  No report or narrative is rewritten; deletions stay unstaged.
.EXAMPLE
  .\project\REMOVE_REDUNDANT_WASTES_SNAPSHOTS.ps1
.EXAMPLE
  .\project\REMOVE_REDUNDANT_WASTES_SNAPSHOTS.ps1 -Apply
#>
[CmdletBinding()]
param([switch]$Apply)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$expectedHead = 'ee49d1dfbc2859c23d2d2f63facf1e784c44f45a'
$repoRoot = (& git -C $PSScriptRoot rev-parse --show-toplevel 2>$null)
if ($LASTEXITCODE -ne 0 -or -not $repoRoot) { throw 'Not inside the expected Git checkout.' }
$repoRoot = [IO.Path]::GetFullPath(($repoRoot | Select-Object -First 1).Trim())
$branch = (& git -C $repoRoot branch --show-current).Trim()
$head = (& git -C $repoRoot rev-parse HEAD).Trim()
if ($branch -ne 'main' -or $head -ne $expectedHead) {
    throw "Repository HEAD/branch changed: $branch $head. Re-audit before deleting."
}
$indexPath = Join-Path $repoRoot 'project/REPORT_SNAPSHOT_RETENTION_INDEX.json'
$logPath = Join-Path $repoRoot 'project/WASTES_CLEANUP_CHANGELOG.md'
if (-not (Test-Path -LiteralPath $indexPath -PathType Leaf) -or
    -not (Test-Path -LiteralPath $logPath -PathType Leaf)) {
    throw 'The retention index and continuing changelog must both exist.'
}
$utf8 = New-Object Text.UTF8Encoding($false)
$index = ConvertFrom-Json -InputObject ([IO.File]::ReadAllText($indexPath, $utf8))
if ($index.schema_version -ne 1) { throw 'Unknown retention index schema.' }
$entries = @($index.tracker_snapshots) + @($index.decision_snapshots) + @($index.arc_baselines)
if ($entries.Count -ne 42 -or
    @($entries | ForEach-Object { $_.path } | Select-Object -Unique).Count -ne 42) {
    throw 'Expected 42 unique, audited entries.'
}
$candidates = @($entries | Where-Object { ([string]$_.retention).StartsWith('conditional_removal_') })
$protected = @($entries | Where-Object { ([string]$_.retention).StartsWith('retain_') })
$removedMarker = 'removed_by_owner_authorized_local_cleanup'
$removedAlready = @($entries | Where-Object { $_.retention -eq $removedMarker })
if ($candidates.Count -eq 0 -and $removedAlready.Count -eq 34 -and $protected.Count -eq 8) {
    Write-Host 'Already completed according to the retention index. No action taken.'
    exit 0
}
if ($candidates.Count -ne 34 -or $protected.Count -ne 8 -or $removedAlready.Count -ne 0) {
    throw "Unexpected selection: $($candidates.Count) candidates, $($protected.Count) protected."
}
function Assert-File($item, [bool]$clean) {
    $relative = [string]$item.path
    if ($relative -notmatch '^research/legacy/[A-Za-z0-9_.-]+\.md$' -or $relative.Contains('..')) {
        throw "Unexpected source path: $relative"
    }
    $absolute = [IO.Path]::GetFullPath((Join-Path $repoRoot $relative))
    $prefix = $repoRoot.TrimEnd('\','/') + [IO.Path]::DirectorySeparatorChar
    if (-not $absolute.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Outside checkout: $relative"
    }
    if (-not (Test-Path -LiteralPath $absolute -PathType Leaf)) {
        throw "Missing expected file: $relative"
    }
    $file = Get-Item -LiteralPath $absolute
    if (($file.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw "Reparse point is not allowed: $relative"
    }
    if ($file.Length -ne [long]$item.size_bytes) {
        throw "Incorrect file size: $relative"
    }
    $actual = (Get-FileHash -LiteralPath $absolute -Algorithm SHA256).Hash
    if (-not $actual.Equals([string]$item.sha256, [StringComparison]::OrdinalIgnoreCase)) {
        throw "SHA-256 mismatch: $relative"
    }
    if ($clean) {
        & git -C $repoRoot ls-files --error-unmatch -- $relative *> $null
        if ($LASTEXITCODE -ne 0) { throw "Not tracked in Git: $relative" }
        $changes = @(& git -C $repoRoot status --porcelain=v1 --untracked-files=all -- $relative)
        if ($LASTEXITCODE -ne 0 -or @($changes | Where-Object { $_ }).Count -gt 0) {
            throw "Candidate contains uncommitted changes: $relative"
        }
    }
    return $absolute
}
# Refuse any filename outside the three exact categories previously reviewed.
foreach ($item in $candidates) {
    $path = [string]$item.path
    $approved = (
        $path -match '^research/legacy/WASTES_CLEANUP_(MANIFEST|PROGRESS)_PRE_(97|98|99_100|101|102|103|104|105|106_107|108|109|110|111|112|113)_2026-10-(28|29)\.md$' -or
        $path -match '^research/legacy/DECISIONS_PRE_D0(49_94|50_102|51_111)_2026-10-(28|29)\.md$' -or
        $path -eq 'research/legacy/ARC_ONE_PRE_ARC02_DRAFT_103_2026-10-29.md'
    )
    if (-not $approved) { throw "Not an approved deletion target: $path" }
}
# Preflight the entire batch before ANY destructive action.
foreach ($item in $candidates) { $null = Assert-File $item $true }
foreach ($item in $protected) { $null = Assert-File $item $false }
# Reject deletion if any live Markdown file has a clickable link to a candidate.
# Historical prose mentions of original filenames are intentionally permitted.
$linkNames = @($candidates | ForEach-Object { [regex]::Escape(([string]$_.path).Split('/')[-1]) })
$linkPattern = '\]\([^)]*(?:' + ($linkNames -join '|') + ')(?:#[^)]*)?\)'
foreach ($markdown in @(Get-ChildItem -LiteralPath $repoRoot -File -Recurse -Filter '*.md')) {
    if ($markdown.FullName -match '[\\/]\.git[\\/]') { continue }
    $body = [IO.File]::ReadAllText($markdown.FullName, $utf8)
    if ([regex]::IsMatch($body, $linkPattern)) {
        throw "A Markdown link still targets a candidate: $($markdown.FullName). Reconcile it first."
    }
}
$bytes = ($candidates | Measure-Object -Property size_bytes -Sum).Sum
Write-Host ("Verified 34 clean candidates, 8 protected originals, {0:N2} MiB redundant." -f ([double]$bytes / 1MB))
if (-not $Apply) {
    Write-Host 'PREVIEW ONLY. Supply -Apply to perform the deletion.'
    foreach ($item in $candidates) { Write-Output ("WOULD REMOVE  " + $item.path) }
    exit 0
}
if ((& git -C $repoRoot rev-parse HEAD).Trim() -ne $expectedHead) {
    throw 'HEAD changed during verification; nothing removed.'
}
$deleted = 0
foreach ($item in $candidates) {
    $absolute = Assert-File $item $true
    Remove-Item -LiteralPath $absolute -Force -ErrorAction Stop
    if (Test-Path -LiteralPath $absolute) { throw "Deletion failed: $($item.path)" }
    $deleted++
}
foreach ($item in $protected) { $null = Assert-File $item $false }
foreach ($item in $candidates) { $item.retention = $removedMarker }
$index.status = 'historical_reference_index_34_archival_removals_completed'
$index.comparison.physical_deletion_completed = $true
$index.historical_resolution | Add-Member -NotePropertyName physical_removal_note -NotePropertyValue '34 hash-verified physical copies removed; paths and historical report evidence retained.' -Force
[IO.File]::WriteAllText($indexPath, ((ConvertTo-Json -InputObject $index -Depth 20) + [Environment]::NewLine), $utf8)
$when = Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz'
$note = [Environment]::NewLine + "**$when - Owner-authorized administrative consolidation:** Removed 34 hash-verified redundant local snapshots (30 intermediate trackers, three decision copies, one duplicate legacy Arc One archive). All original path/size/hash records remain in [the retention index](REPORT_SNAPSHOT_RETENTION_INDEX.json). Eight protected baselines and historical reports remain unchanged. Git deletions are unstaged; no commit, push, narrative, audio, or public navigation change." + [Environment]::NewLine
[IO.File]::AppendAllText($logPath, $note, $utf8)
Write-Host "Removed $deleted files, updated index and changelog. Review unstaged deletions:"
& git -C $repoRoot status --short
