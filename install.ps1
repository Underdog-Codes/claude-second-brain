# Claude Brain Template - Installer
# Right-click this file and select "Run with PowerShell"

Write-Host "`n  Claude Brain Template - Installer`n  ==================================`n"

# Install Python if not found
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "  [1/2] Installing Python..."
    winget install Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements
} else {
    Write-Host "  [1/2] Python already installed - skipping."
}

# Run setup
Write-Host "  [2/2] Running setup...`n"
python setup.py

Write-Host "`n  Press any key to close..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
