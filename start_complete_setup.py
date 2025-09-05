#!/usr/bin/env python3
"""
UBS Coding Challenge 2025 - Complete Setup Script
Starts both Flask API server and participant frontend
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def start_complete_setup():
    print("🏆 UBS Coding Challenge 2025 - Complete Setup")
    print("=" * 60)
    
    project_root = Path(__file__).parent
    
    print("🚀 Starting Flask API Server...")
    flask_process = subprocess.Popen([
        sys.executable, "app.py"
    ], cwd=project_root / "flask_app")
    
    # Wait for Flask to start
    time.sleep(3)
    
    print("🌐 Starting Participant Frontend...")
    frontend_process = subprocess.Popen([
        sys.executable, "start_frontend.py"
    ], cwd=project_root / "web_frontend")
    
    print("\n✅ Both servers are starting!")
    print("=" * 60)
    print("🔗 Flask API: http://localhost:5000")
    print("🌐 Participant Frontend: http://localhost:8080")
    print("📚 API Documentation: http://localhost:5000/api/")
    print("🏥 Health Check: http://localhost:5000/health")
    print("=" * 60)
    print("\n📋 Instructions for Participants:")
    print("1. Open http://localhost:8080 in your browser")
    print("2. Enter your name")
    print("3. Browse challenges and submit solutions")
    print("4. Compete on the live leaderboard!")
    print("\nPress Ctrl+C to stop both servers")
    print("=" * 60)
    
    try:
        # Wait for both processes
        flask_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down servers...")
        flask_process.terminate()
        frontend_process.terminate()
        flask_process.wait()
        frontend_process.wait()
        print("✅ All servers stopped successfully")

if __name__ == "__main__":
    start_complete_setup()
