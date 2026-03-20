# Push selection_data_to_paste_in_supabase.json to Supabase.
# Updates the selections table so the website shows the correct data.

$url = "https://mcvkkohtvywwvtndpuvw.supabase.co/rest/v1/selections?id=eq.main"
$key = "sb_publishable_WN9vSmDmDJTTXE5uMP0lzQ_yl_ak5tL"
$jsonPath = Join-Path $PSScriptRoot "selection_data_to_paste_in_supabase.json"

if (-not (Test-Path $jsonPath)) {
    Write-Host "File not found: $jsonPath" -ForegroundColor Red
    exit 1
}

$data = Get-Content $jsonPath -Raw -Encoding UTF8 | ConvertFrom-Json
$body = @{
    data = $data
    updated_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.fffZ")
} | ConvertTo-Json -Depth 100 -Compress

$headers = @{
    "apikey" = $key
    "Authorization" = "Bearer $key"
    "Content-Type" = "application/json"
    "Prefer" = "return=minimal"
}

try {
    $resp = Invoke-WebRequest -Uri $url -Method PATCH -Headers $headers -Body $body -UseBasicParsing
    if ($resp.StatusCode -eq 200 -or $resp.StatusCode -eq 204) {
        Write-Host "Selections pushed to Supabase successfully." -ForegroundColor Green
        Write-Host "Refresh the selections page (Ctrl+Shift+R) to see the updates." -ForegroundColor Cyan
    } else {
        Write-Host "Unexpected status: $($resp.StatusCode)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "Push failed: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $reader.BaseStream.Position = 0
        $reader.DiscardBufferedData()
        Write-Host $reader.ReadToEnd() -ForegroundColor Red
    }
    exit 1
}
