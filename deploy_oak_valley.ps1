# Deploy deploy_live to oak-valley-estates.pages.dev
# Both sites MUST use the same folder (deploy_live) to show identical content
$envFile = Join-Path $PSScriptRoot ".env.cloudflare"
if (Test-Path $envFile) {
    $line = Get-Content $envFile | Select-Object -First 1
    if ($line -match 'CLOUDFLARE_API_TOKEN=(.+)') { $env:CLOUDFLARE_API_TOKEN = $matches[1].Trim() }
}
npx wrangler pages deploy deploy_live --project-name=oak-valley-estates
