# setup_windows.ps1 — Setup cross-platform computer-use on Windows
Write-Host "=== Computer Use Skill — Windows Setup ===" -ForegroundColor Cyan

# Check Python
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command python3 -ErrorAction SilentlyContinue
}
if (-not $python) {
    Write-Host "❌ Python not found. Install from https://python.org" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Python: $($python.Source)"

# Install dependencies
Write-Host "`nInstalling pyautogui and Pillow..."
& $python.Source -m pip install --upgrade pyautogui Pillow 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ pip install failed" -ForegroundColor Red
    exit 1
}

# Verify
Write-Host "Verifying..."
& $python.Source -c "import pyautogui; s=pyautogui.size(); print(f'✅ pyautogui works — screen {s.width}x{s.height}')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ pyautogui verification failed" -ForegroundColor Red
    exit 1
}

Write-Host "`n✅ All set! You can now use the cross-platform scripts." -ForegroundColor Green
