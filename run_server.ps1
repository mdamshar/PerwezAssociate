# Perwez Associate - Django Development Server Startup Script (PowerShell)

Write-Host ""
Write-Host "========================================"
Write-Host "Perwez Associate - Development Server"
Write-Host "========================================"
Write-Host ""

# Check if Python is installed
try {
    python --version | Out-Null
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Checking dependencies..."
pip install -q -r requirements.txt

Write-Host ""
Write-Host "Running Django checks..."
python manage.py check

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Django configuration check failed" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Server is starting..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Access the website at:" -ForegroundColor Cyan
Write-Host "  http://localhost:8000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Admin panel at:" -ForegroundColor Cyan
Write-Host "  http://localhost:8000/admin" -ForegroundColor Yellow
Write-Host ""
Write-Host "Admin Credentials:" -ForegroundColor Cyan
Write-Host "  Username: admin" -ForegroundColor Yellow
Write-Host "  Password: admin123" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

python manage.py runserver
