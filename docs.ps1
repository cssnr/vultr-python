param (
    [switch]$c,
    [switch]$b
)

$ErrorActionPreference = "Stop"

write-output "Clean:    $c"
write-output "Build:    $b"

if ($c) {
    Write-Host -ForegroundColor Yellow "Cleaning Docs..."
    $site_dir = ".\site"
    if (Test-Path $site_dir) {
        Write-Host -ForegroundColor Cyan "Removing: $site_dir"
        Remove-Item -Force -Recurse $site_dir
    }
    $cache_dir = ".\.cache"
    if (Test-Path $cache_dir) {
        Write-Host -ForegroundColor Cyan "Removing: $cache_dir"
        Remove-Item -Force -Recurse $cache_dir
    }
}

python -m pdoc -t .\docs\ -p 8008 `
    --favicon "https://df.cssnr.com/raw/logo128.png" `
    --logo "https://df.cssnr.com/raw/logo128.png" `
    --logo-link "https://github.com/cssnr/vultr-python" `
    vultr

#-e "vultr=https://github.com/cssnr/vultr-python/blob/updates/src/vultr/" `

#if ($b) {
#    Write-Host -ForegroundColor Green "Building Docs..."
#    zensical build
#} else {
#    zensical serve
#}
