# Research Agent Skills installer (Windows PowerShell 5.1+ / PowerShell 7) - Kalaris Labs
#
#   irm https://raw.githubusercontent.com/KalarisLabs/research-agent-skills/main/install.ps1 | iex
#
# Options (environment variables):
#   RAS_VERSION   release to install, e.g. 1.0.0 (default: latest)
#   RAS_BUNDLE    bundle or category (default: research-essentials; "all" for everything)
#   RAS_HARNESS   auto | all | comma list: claude-code,codex,cursor,gemini-cli,copilot,opencode,windsurf,agents
#   RAS_NO_NODE   set to 1 to force the standalone (no Node.js) installer
#   RAS_BASE_URL  release download base URL (testing/mirrors); default GitHub Releases
#
# With Node.js >= 18 this delegates to the npm CLI. Without Node it downloads the
# release tarball, verifies its SHA-256 against the release SHA256SUMS,
# and copies the selected skills into place.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 3

$Repo = 'KalarisLabs/research-agent-skills'
$Version = if ($env:RAS_VERSION) { $env:RAS_VERSION } else { 'latest' }
$Bundle = if ($env:RAS_BUNDLE) { $env:RAS_BUNDLE } else { 'research-essentials' }
$Harness = if ($env:RAS_HARNESS) { $env:RAS_HARNESS } else { 'auto' }

if ($Version -notmatch '^(latest|\d[\w.\-]*)$') { throw "invalid RAS_VERSION '$Version'" }
if ($Bundle -notmatch '^[a-z0-9-]+$') { throw "invalid RAS_BUNDLE '$Bundle'" }

$node = Get-Command node -ErrorAction SilentlyContinue
$npx = Get-Command npx -ErrorAction SilentlyContinue
if ($node -and $npx -and $env:RAS_NO_NODE -ne '1') {
  $major = [int]((& node -p 'process.versions.node').Split('.')[0])
  if ($major -ge 18) {
    $sel = if ($Bundle -eq 'all') { @('--all') } elseif ($Bundle -in @('research-essentials', 'ml-research', 'ai-research', 'biology-research', 'chemistry-research', 'medicine-research', 'physics-research')) { @('--bundle', $Bundle) } else { @('--category', $Bundle) }
    Write-Host 'Installing with the research-agent-skills CLI (npm)...'
    & npx -y "research-agent-skills@$Version" install @sel --harness $Harness --yes
    exit $LASTEXITCODE
  }
}

Write-Host 'Node.js 18+ not found; using the standalone installer.'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
if ($Version -eq 'latest' -and -not $env:RAS_BASE_URL) {
  $rel = Invoke-RestMethod -UseBasicParsing -Headers @{ 'User-Agent' = 'research-agent-skills-installer' } "https://api.github.com/repos/$Repo/releases/latest"
  $Version = $rel.tag_name -replace '^v', ''
}
$tmp = Join-Path ([IO.Path]::GetTempPath()) ("ras-" + [Guid]::NewGuid())
New-Item -ItemType Directory -Path $tmp | Out-Null
try {
  $asset = "research-agent-skills-$Version.tar.gz"
  $base = if ($env:RAS_BASE_URL) { $env:RAS_BASE_URL } else { "https://github.com/$Repo/releases/download/v$Version" }
  Write-Host "Downloading $asset ..."
  foreach ($file in @($asset, 'SHA256SUMS')) {
    $source = [Uri]("$base/$file")
    $destination = Join-Path $tmp $file
    if ($source.IsFile) {
      Copy-Item -LiteralPath $source.LocalPath -Destination $destination
    } else {
      Invoke-WebRequest -UseBasicParsing $source.AbsoluteUri -OutFile $destination
    }
  }
  $line = Get-Content (Join-Path $tmp 'SHA256SUMS') | Where-Object { $_ -match "^([0-9a-f]{64})\s+\*?$([regex]::Escape($asset))$" } | Select-Object -First 1
  if (-not $line) { throw "SHA256SUMS has no entry for $asset" }
  $expected = ($line -split '\s+')[0].ToLower()
  $actual = (Get-FileHash -Algorithm SHA256 (Join-Path $tmp $asset)).Hash.ToLower()
  if ($expected -ne $actual) { throw "checksum mismatch for $asset" }
  Write-Host "Verified SHA-256 $actual"

  $x = Join-Path $tmp 'x'
  New-Item -ItemType Directory -Path $x | Out-Null
  & tar -xzf (Join-Path $tmp $asset) -C $x --strip-components=1
  if ($LASTEXITCODE -ne 0) { throw 'tar extraction failed (Windows 10 1803+ ships tar.exe)' }
  $list = Join-Path $x "catalog/lists/$Bundle.txt"
  if (-not (Test-Path $list)) { throw "unknown bundle or category '$Bundle'" }

  $h = if ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
  $map = [ordered]@{
    'claude-code' = @("$h\.claude", "$h\.claude\skills"); 'codex' = @("$h\.codex", "$h\.codex\skills")
    'cursor' = @("$h\.cursor", "$h\.cursor\skills"); 'gemini-cli' = @("$h\.gemini", "$h\.gemini\skills")
    'copilot' = @("$h\.copilot", "$h\.copilot\skills"); 'opencode' = @("$h\.config\opencode", "$h\.config\opencode\skills")
    'windsurf' = @("$h\.codeium\windsurf", "$h\.codeium\windsurf\skills"); 'agents' = @("$h\.agents", "$h\.agents\skills")
  }
  $targets = New-Object System.Collections.Generic.List[string]
  foreach ($id in $Harness.Split(',')) {
    $id = $id.Trim()
    if ($id -eq 'auto') {
      foreach ($k in $map.Keys) { if ($k -ne 'agents' -and (Test-Path $map[$k][0])) { $targets.Add($map[$k][1]) } }
      if ($targets.Count -eq 0) { $targets.Add($map['claude-code'][1]) }
    } elseif ($id -eq 'all') {
      foreach ($k in $map.Keys) { $targets.Add($map[$k][1]) }
    } elseif ($map.Contains($id)) {
      $targets.Add($map[$id][1])
    } else { throw "unknown harness '$id'" }
  }
  $count = 0
  foreach ($dir in ($targets | Select-Object -Unique)) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    foreach ($name in Get-Content $list) {
      if ($name -notmatch '^[a-z0-9-]+$') { continue }
      $dest = Join-Path $dir $name
      if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
      Copy-Item -Recurse (Join-Path $x "skills/$name") $dest
      $count++
    }
    Write-Host "  installed into $dir"
  }
  Write-Host "Installed $count skill copies (v$Version, $Bundle). Restart your agent to load them."
} finally {
  Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
