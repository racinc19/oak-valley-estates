# Backup Supabase selections data to a local JSON file.
# Run regularly (e.g. weekly) or before big changes.
# Restore: paste file contents into Supabase Table Editor > selections > row main > data column.

$url = "https://mcvkkohtvywwvtndpuvw.supabase.co/rest/v1/selections?id=eq.main&select=data"
$key = "sb_publishable_WN9vSmDmDJTTXE5uMP0lzQ_yl_ak5tL"

$headers = @{
  "apikey" = $key
  "Authorization" = "Bearer $key"
}

try {
  $resp = Invoke-RestMethod -Uri $url -Headers $headers -Method Get
  $data = if ($resp -is [array] -and $resp.Count -gt 0) { $resp[0].data } else { $resp.data }
  if ($data) {
    $outDir = Join-Path $PSScriptRoot "backups"
    if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
    $name = "selections_backup_" + (Get-Date -Format "yyyy-MM-dd_HHmm") + ".json"
    $path = Join-Path $outDir $name
    $data | ConvertTo-Json -Depth 100 -Compress | Set-Content $path -Encoding UTF8
    Write-Host "Saved: $path"
  } else {
    Write-Host "No data in Supabase (row main)." -ForegroundColor Yellow
  }
} catch {
  Write-Host "Fetch failed (check RLS/key). Use manual backup:" -ForegroundColor Yellow
  Write-Host "Supabase > Table Editor > selections > row main > copy data cell"
}
