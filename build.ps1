param (
    [switch]$c,
    [switch]$i,
    [switch]$u
)

$ErrorActionPreference = "Stop"

write-output "Clean:      $c"
write-output "Install:    $i"
write-output "Uninstall:  $u"

if ($u) {
    Write-Host -ForegroundColor Red "Uninstalling..."
    python -m pip uninstall -y vultr-python
}

$egg_dir = ".\src\*.egg-info"
if (Test-Path $egg_dir) {
    Write-Host -ForegroundColor Cyan "Removing: $egg_dir"
    Remove-Item -Force -Recurse $egg_dir
}
$cache_dir = ".\src\*\__pycache__"
if (Test-Path $cache_dir) {
    Write-Host -ForegroundColor Cyan "Removing: $cache_dir"
    Remove-Item -Force -Recurse $cache_dir
}
if (Test-Path ".\dist") {
    Write-Host -ForegroundColor Cyan "Removing: .\dist"
    Remove-Item -Force -Recurse ".\dist"
}
if (Test-Path ".\build") {
    Write-Host -ForegroundColor Cyan "Removing: .\build"
    Remove-Item -Force -Recurse ".\build"
}
if ($c) {
    Write-Host -ForegroundColor Yellow "Clean Only. Not Building or Installing!"
    exit
}

python -m build

if ($args[0] -eq "i") {
    Write-Host -ForegroundColor Green "Installing..."
    python -m pip install .\dist\vultr_python-0.0.1-py3-none-any.whl
}

Write-Output "Success."
