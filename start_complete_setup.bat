@echo off
title UBS Coding Challenge 2025 - Complete Setup

echo ================================================
echo  UBS Coding Challenge 2025 - Complete Setup
echo ================================================
echo.
echo Starting both servers for the coding challenge:
echo.
echo 1. Flask API Server (Backend) - Port 5000
echo 2. Participant Frontend (Web UI) - Port 8080
echo.
echo The participant frontend will open automatically
echo Press Ctrl+C to stop both servers
echo ================================================

cd /d "%~dp0"

C:/Users/teren/AppData/Local/Programs/Python/Python313/python.exe start_complete_setup.py

echo.
echo All servers stopped.
pause
