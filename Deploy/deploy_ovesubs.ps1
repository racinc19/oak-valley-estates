# Deploy deploy_ovesubs to ovesubs.pages.dev
# Optionally syncs selections from deploy_live (Oak Valley) so subs see same selections as client
$envFile = Join-Path $PSScriptRoot ".env.cloudflare"
if (Test-Path $envFile) {
    $line = Get-Content $envFile | Select-Object -First 1
    if ($line -match 'CLOUDFLARE_API_TOKEN=(.+)') { $env:CLOUDFLARE_API_TOKEN = $matches[1].Trim() }
}
$syncScript = Join-Path $PSScriptRoot "sync_selections.ps1"
if (Test-Path $syncScript) { & $syncScript }
else { Write-Host "Note: sync_selections.ps1 not found; skip selections sync" }
$repo = Split-Path $PSScriptRoot -Parent
Set-Location $repo
npx wrangler pages deploy Deploy/deploy_ovesubs --project-name=ovesubs
