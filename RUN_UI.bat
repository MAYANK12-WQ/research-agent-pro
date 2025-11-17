@echo off
echo ========================================
echo Research Agent Pro - UI Launcher
echo ========================================
echo.

cd frontend

echo Step 1: Installing dependencies...
echo (This may take 2-3 minutes)
echo.

call npm install

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: npm install failed!
    echo Try running as Administrator or:
    echo 1. Close all running processes
    echo 2. Run: npm cache clean --force
    echo 3. Try again
    pause
    exit /b 1
)

echo.
echo Step 2: Starting development server...
echo.
echo The UI will open at: http://localhost:3000
echo.

call npm run dev

pause
