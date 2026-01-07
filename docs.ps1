param (
    [switch]$c,
    [switch]$b,
    [switch]$w
)

$ErrorActionPreference = "Stop"

write-output "Clean:    $c"
write-output "Build:    $b"
write-output "Watch:    $w"

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

$logo = "https://raw.githubusercontent.com/cssnr/vultr-python/refs/heads/master/.github/assets/logo.svg"
$logoLink = "https://github.com/cssnr/vultr-python"

if ($b)
{
    Write-Host -ForegroundColor Yellow "Building Docs..."
    python -m pdoc -t .\docs\ -o site `
        --logo $logo --logo-link $logoLink vultr
}
elseif ($w) {
    Write-Host -ForegroundColor Green "Watching Docs..."
    watchmedo auto-restart -R -d .\docs\ -p "*.*" -- `
        python -m pdoc -t .\docs\ -p 8000 -h 0.0.0.0 `
            --logo $logo --logo-link $logoLink .\src\vultr\
} else {
    Write-Host -ForegroundColor Green "Serving Docs..."
    python -m pdoc -t .\docs\ -p 8000 -h 0.0.0.0 `
        --logo $logo --logo-link $logoLink .\src\vultr\
}

#--favicon "https://df.cssnr.com/raw/logo128.png" `
#-e "vultr=https://github.com/cssnr/vultr-python/blob/updates/src/vultr/" `
