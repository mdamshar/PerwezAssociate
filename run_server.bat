@echo off
REM Perwez Associate - Django Development Server Startup Script
REM This script automatically installs dependencies and starts the development server

cd /d "%~dp0"

echo.
echo ========================================
echo Perwez Associate - Development Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Checking dependencies...
pip install -q -r requirements.txt

echo.
echo Running Django checks...
python manage.py check

if errorlevel 1 (
    echo ERROR: Django configuration check failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo Server is starting...
echo ========================================
echo.
echo Access the website at:
echo   http://localhost:8000
echo.
echo Admin panel at:
echo   http://localhost:8000/admin
echo.
echo Admin Credentials:
echo   Username: admin
echo   Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python manage.py runserver

pause
