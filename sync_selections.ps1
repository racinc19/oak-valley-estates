# Copy Oak Valley selections (deploy_live) to OVE Subs (deploy_ovesubs)
# Run before deploying ovesubs so subs see the same selections as client
# Then replace nav with OVE Subs nav (Dashboard, Plans & Permits, Selections)
Copy-Item Deploy/deploy_live\selections.html Deploy/deploy_ovesubs\selections.html -Force
$c = Get-Content Deploy/deploy_ovesubs\selections.html -Raw
$oveNav = @'
<nav class="topnav"><div class="topnav-inner">
  <a href="index.html" class="topnav-brand"><span class="dot"></span>Rodriguez Residence</a>
  <div class="topnav-links">
    <a href="index.html" style="padding:8px 14px;border-radius:8px;font-size:13px;font-weight:700;color:#fff;background:var(--blue);text-decoration:none">Dashboard</a>
    <a href="https://drive.google.com/drive/u/0/folders/1kS-2awScLDAnGS973xD0D28RxynI49Si" target="_blank" style="padding:8px 14px;border-radius:8px;font-size:13px;font-weight:600;color:var(--cyan);text-decoration:none;border:1px solid rgba(6,182,212,.3)">📁 Plans & Permits</a>
    <a href="selections.html" style="padding:8px 14px;border-radius:8px;font-size:13px;font-weight:600;color:var(--purple);text-decoration:none;border:1px solid rgba(139,92,246,.3)">🎨 Selections</a>
  </div>
  <div class="topnav-right">
    <button class="topnav-btn" onclick="location.reload()">↻ Refresh</button>
  </div>
</div></nav>
'@
$pattern = '(?s)<nav class="topnav">.*?</nav>'
$c = $c -replace $pattern, $oveNav.Trim()
# Add OVE Subs nav CSS if missing
if ($c -notmatch '\.topnav-right') {
  $navCss = ".topnav-right{display:flex;gap:8px;align-items:center;margin-left:auto}.topnav-btn{padding:6px 14px;border-radius:8px;font-size:12px;font-weight:500;border:1px solid var(--bdr);background:none;color:var(--txt2);cursor:pointer;transition:all .2s;white-space:nowrap}.topnav-btn:hover{border-color:var(--blue);color:var(--txt)}"
  $c = $c -replace '</style>', "$navCss`n</style>"
}
Set-Content Deploy/deploy_ovesubs\selections.html -Value $c -NoNewline
Write-Host "Synced selections.html to deploy_ovesubs (OVE Subs nav)"
