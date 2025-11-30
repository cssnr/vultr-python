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

if ($b) {
    Write-Host -ForegroundColor Yellow "Building Docs..."
    python -m pdoc -t .\docs\ -o site `
    --logo "https://raw.githubusercontent.com/cssnr/vultr-python/refs/heads/master/.github/assets/logo.svg" `
    --logo-link "https://github.com/cssnr/vultr-python" `
    vultr
} else {
    Write-Host -ForegroundColor Green "Serving Docs..."
    python -m pdoc -t .\docs\ -p 8000 -h 0.0.0.0 `
    --logo "https://raw.githubusercontent.com/cssnr/vultr-python/refs/heads/master/.github/assets/logo.svg" `
    --logo-link "https://github.com/cssnr/vultr-python" `
    vultr
}

#--favicon "https://df.cssnr.com/raw/logo128.png" `
#-e "vultr=https://github.com/cssnr/vultr-python/blob/updates/src/vultr/" `
