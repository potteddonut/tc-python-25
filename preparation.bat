@echo off
setlocal

:: ========================================
::  Install Python 3.12 and pygame on Windows
:: ========================================

set "PYTHON_VERSION=3.12.6"
set "PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe"
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%"

echo ========================================
echo Downloading Python %PYTHON_VERSION% installer...
echo ========================================

powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'"

echo.
echo ========================================
echo Installing Python silently with pip and Add to PATH...
echo ========================================

:: /quiet = silent install
:: InstallAllUsers=1 = system-wide install
:: PrependPath=1 = add to PATH
:: Include_pip=1 = install pip
"%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1

:: Wait a moment for PATH to update
timeout /t 5 /nobreak >nul

echo.
echo ========================================
echo Verifying Python installation...
echo ========================================
python --version
if errorlevel 1 (
    echo Python installation failed.
    exit /b 1
)

echo.
echo ========================================
echo Upgrading pip...
echo ========================================
python -m pip install --upgrade pip

echo.
echo ========================================
echo Installing pygame...
echo ========================================
python -m pip install pygame

echo.
echo ========================================
echo Installation complete!
echo Testing pygame...
echo ========================================
python -m pygame.examples.aliens

echo.
echo Done!
pause
endlocal
