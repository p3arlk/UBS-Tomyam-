@echo off
echo UBS Coding Challenge 2025 - Quick Start
echo ========================================
echo.
echo Select which server to start:
echo 1. Flask Server (http://localhost:5000)
echo 2. FastAPI Server (http://localhost:8000)
echo 3. Both Servers
echo.
set /p choice="Enter your choice (1-3): "

cd /d "%~dp0"

if "%choice%"=="1" (
    echo Starting Flask server...
    cd flask_app
    C:/Users/teren/AppData/Local/Programs/Python/Python313/python.exe app.py
) else if "%choice%"=="2" (
    echo Starting FastAPI server...
    cd fastapi_app
    C:/Users/teren/AppData/Local/Programs/Python/Python313/python.exe -m uvicorn main:app --reload --port 8000
) else if "%choice%"=="3" (
    echo Starting both servers...
    start "Flask Server" cmd /k "cd flask_app && C:/Users/teren/AppData/Local/Programs/Python/Python313/python.exe app.py"
    start "FastAPI Server" cmd /k "cd fastapi_app && C:/Users/teren/AppData/Local/Programs/Python/Python313/python.exe -m uvicorn main:app --reload --port 8000"
    echo Both servers are starting in separate windows...
    echo Flask: http://localhost:5000
    echo FastAPI: http://localhost:8000 (docs: http://localhost:8000/docs)
) else (
    echo Invalid choice. Please run the script again.
)

pause
