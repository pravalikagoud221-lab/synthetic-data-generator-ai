@echo off
echo =====================================================
echo   Synthetic Data Generator - Ollama Edition
echo =====================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo Python found: 
for /f "tokens=*" %%i in ('python --version') do echo %%i

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo =====================================================
echo Setup complete!
echo =====================================================
echo.
echo Starting Flask application...
echo.
echo Open your browser to: http://localhost:5000
echo.
echo Make sure Ollama is running in another terminal:
echo    ollama pull mistral
echo    ollama serve
echo.
echo Press Ctrl+C to stop the application
echo =====================================================
echo.

python app.py
pause
