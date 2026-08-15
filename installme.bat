@echo off
echo ===================================================
echo   🏔️ Visit Nepal 2022 Installer (Windows)
echo ===================================================
echo.

:: Check Python installation
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not added to PATH.
    echo Please install Python 3.9+ from https://python.org and try again.
    pause
    exit /b 1
)

echo 📦 Creating Python virtual environment (venv)...
python -m venv venv
if %errorlevel% neq 0 (
    echo ❌ Failed to create virtual environment.
    pause
    exit /b 1
)
echo.

echo 🔌 Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo ❌ Failed to activate virtual environment.
    pause
    exit /b 1
)
echo.

echo 🔄 Upgrading pip...
python -m pip install --upgrade pip
echo.

echo 📥 Installing project dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies.
    pause
    exit /b 1
)
echo.

echo 🗄️ Setting up database and migrations...
cd django_app
python manage.py migrate
if %errorlevel% neq 0 (
    echo ⚠️ Database migration had issues. Continuing...
)
cd ..
echo.

echo ===================================================
echo 🎉 Installation Completed Successfully!
echo ===================================================
echo.
echo To run the application:
echo 1. Run "venv\Scripts\activate" to activate virtual environment.
echo 2. Run "python run_all.py" to start Django and Rasa.
echo.
pause
