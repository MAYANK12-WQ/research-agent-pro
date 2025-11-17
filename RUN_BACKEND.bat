@echo off
echo ============================================
echo Research Agent Pro - Backend Server
echo ============================================
echo.

cd backend

echo Checking environment...
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please copy .env.example to .env and add your API keys
    pause
    exit /b 1
)

echo.
echo Starting backend server...
echo Backend will run on: http://localhost:8000
echo API Docs will be at: http://localhost:8000/docs
echo.

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
