# Ship OVE subs → Cloudflare Pages: copy Deploy/deploy_ovesubs into a local clone of
#   https://github.com/racinc19/ovesubs
# then commit + push THAT repo (the one the dashboard is actually connected to).
# Optional: also commit/push this monorepo to keep it in lockstep.
# Run:  powershell -File "…\Deploy\ship_ove_subs.ps1"
#
# Layout that works with zero config: clone ovesubs as a sibling of this repo:
#   Desktop\Oak-Valley-Estates\  (this repo)
#   Desktop\ovesubs\             (clone of racinc19/ovesubs)
# Or set a path in Deploy/ove_subs_sync_target.txt (one non-comment line).

[CmdletBinding()]
param(
  [string]$Message = "Sync OVE subs from Oak-Valley-Estates/Deploy/deploy_ovesubs",
  [string]$OveSubsPath = "",

  [switch]$AlsoPushSourceRepo,
  [string]$SourceMessage = "",

  [switch]$WithWrangler
)

$ErrorActionPreference = 'Stop'
$here = $PSScriptRoot
$repoRoot = Split-Path $here -Parent
$sourceSite = Join-Path $repoRoot 'Deploy\deploy_ovesubs'
$config = Join-Path $here 'ove_subs_sync_target.txt'
$liveUrl = 'https://ovesubs.pages.dev'

function Get-OveSubsClone {
  if ($OveSubsPath) {
    $p = $OveSubsPath.Trim()
    if (-not [System.IO.Path]::IsPathRooted($p)) {
      $p = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $p))
    }
    return $p
  }
  if (Test-Path $config) {
    foreach ($line in Get-Content $config) {
      $s = $line.Trim()
      if (-not $s -or $s.StartsWith('#')) { continue }
      if (-not [System.IO.Path]::IsPathRooted($s)) {
        $s = [System.IO.Path]::GetFullPath((Join-Path $repoRoot $s))
      }
      return $s
    }
  }
  $sibling = Join-Path (Split-Path $repoRoot) 'ovesubs'
  if (Test-Path (Join-Path $sibling '.git')) { return $sibling }
  return $null
}

function Test-RobocopyOK {
  param([int]$Code)
  $Code -le 7
}

if (-not (Test-Path $sourceSite)) { Write-Error "Missing: $sourceSite"; exit 1 }
if (-not (Test-Path (Join-Path $repoRoot '.git'))) { Write-Error "Not a git repo: $repoRoot"; exit 1 }

$dest = Get-OveSubsClone
if (-not $dest) {
  Write-Error @"
Could not find the local ovesubs clone.

  Option A: Clone and put it next to this repo:
    git clone https://github.com/racinc19/ovesubs  (parent folder: $(Split-Path $repoRoot -Parent))
    (creates: $(Join-Path (Split-Path $repoRoot) 'ovesubs') )

  Option B: Add the folder path in:
    $config
  (one line; may be relative to Oak-Valley-Estates, e.g.  ..\ovesubs  )

  Option C: Pass -OveSubsPath C:\path\to\ovesubs
"@
  exit 1
}

$dest = [System.IO.Path]::GetFullPath($dest)
if (-not (Test-Path (Join-Path $dest '.git'))) {
  Write-Error "Not a git repository: $dest"
  exit 1
}

# The racinc19/ovesubs package repo serves Cloudflare from Deploy/site_ove (see that repo’s wrangler.toml + Pages project).
# Copying to repo root was a no-op for https://ovesubs.pages.dev
$siteOut = Join-Path $dest 'Deploy\site_ove'
if (-not (Test-Path $siteOut)) {
  $null = New-Item -ItemType Directory -Force -Path $siteOut
  Write-Warning "Created $siteOut (ove subs build output; ok if new)"
}

# --- 1) Mirror site files into the folder Cloudflare actually publishes
Write-Host "Copy from:`n  $sourceSite`n  ->`n  $siteOut`n"
robocopy $sourceSite $siteOut /E /NFL /NDL /NJH /NJS /R:1 /W:1 /IS /IT | Out-Null
$rc = $LASTEXITCODE
if (-not (Test-RobocopyOK -Code $rc)) {
  Write-Error "robocopy failed with code $rc"
  exit 1
}

# --- 2) Commit + push the connected GitHub repo (drives Cloudflare)
Set-Location $dest
$branchOve = (git rev-parse --abbrev-ref HEAD 2>$null)
if (-not $branchOve) { Write-Error "git failed in $dest"; exit 1 }

git add -A
git diff --cached --quiet
if ($LASTEXITCODE -eq 1) {
  git commit -m $Message
} else {
  Write-Warning "No new changes in $dest to commit (copy matched repo or no diff)."
}

Write-Host "Pushing ove subs package repo: $dest  (branch $branchOve) → origin"
& git -C $dest push origin $branchOve
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Pushed. Cloudflare Pages (repo racinc19/ovesubs) should build. Live: $liveUrl"

# --- 3) Optional: save the same state in the monorepo
if ($AlsoPushSourceRepo) {
  Set-Location $repoRoot
  $m = if ($SourceMessage) { $SourceMessage } else { "OVE subs: $(Get-Date -Format 'yyyy-MM-dd HH:mm')" }
  git add -- 'Deploy/deploy_ovesubs'
  $st = git diff --cached --name-only
  if ($st) { git commit -m $m } else { Write-Warning "Monorepo: nothing to commit under Deploy/deploy_ovesubs" }
  $b = (git rev-parse --abbrev-ref HEAD 2>$null)
  if ($b) { git push origin $b; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }
}

# --- 4) Optional: local Wrangler to ovesubs project (same folder name in CF as API deploy - rarely needed)
if ($WithWrangler) {
  $deploy = Join-Path $here 'deploy_ovesubs.ps1'
  if (-not (Test-Path $deploy)) { Write-Error "Missing $deploy"; exit 1 }
  Write-Warning 'Optional wrangler deploy: git push to origin is usually enough.'
  Set-Location $repoRoot
  & $deploy
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

Write-Host "Done."
exit 0
