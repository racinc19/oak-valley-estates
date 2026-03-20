# Deploy deploy_ovesubs to ovesubs.pages.dev
# Syncs selections from deploy_live (Oak Valley) first so subs see same selections as client
$envFile = Join-Path $PSScriptRoot ".env.cloudflare"
if (Test-Path $envFile) {
    $line = Get-Content $envFile | Select-Object -First 1
    if ($line -match 'CLOUDFLARE_API_TOKEN=(.+)') { $env:CLOUDFLARE_API_TOKEN = $matches[1].Trim() }
}
& "$PSScriptRoot\sync_selections.ps1"
npx wrangler pages deploy deploy_ovesubs --project-name=ovesubs
