@echo off
title UBS Coding Challenge 2025 - Flask Server

echo ================================================
echo  UBS Coding Challenge 2025 - Flask Server
echo ================================================
echo.
echo Starting Flask server for coding challenge...
echo Server will be available at: http://localhost:5000
echo API endpoints at: http://localhost:5000/api/
echo.
echo Press Ctrl+C to stop the server
echo ================================================

cd /d "%~dp0\flask_app"

C:/Users/teren/AppData/Local/Programs/Python/Python313/python.exe app.py

echo.
echo Server stopped.
pause
