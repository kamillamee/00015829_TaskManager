# SSH connect to Azure VM


$keyPath = Join-Path $PSScriptRoot "cloudcomputing_key"
$vmHost = "20.251.154.94"
$user = "taskmanagervm"

if (-not (Test-Path $keyPath)) {
    Write-Host "Key not found at $keyPath" -ForegroundColor Red
    exit 1
}

Write-Host "Connecting to ${user}@${vmHost} ..." -ForegroundColor Cyan
ssh -i $keyPath "${user}@${vmHost}"
