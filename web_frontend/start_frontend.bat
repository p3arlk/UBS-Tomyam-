@echo off
title UBS Coding Challenge 2025 - Participant Frontend

echo ================================================
echo  UBS Coding Challenge 2025 - Participant Web
echo ================================================
echo.
echo Starting web frontend for participants...
echo.
echo Frontend will be available at: http://localhost:8080
echo Make sure Flask server is running at: http://localhost:5000
echo.
echo The browser will open automatically
echo Press Ctrl+C to stop the server
echo ================================================

cd /d "%~dp0"

C:/Users/teren/AppData/Local/Programs/Python/Python313/python.exe start_frontend.py

echo.
echo Frontend server stopped.
pause
