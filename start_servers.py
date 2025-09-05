#!/usr/bin/env python3
"""
Startup script for the UBS Coding Challenge servers
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask, fastapi, uvicorn, pytest
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependencies: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def start_flask_server():
    """Start the Flask server"""
    print("Starting Flask server...")
    flask_dir = Path(__file__).parent / "flask_app"
    os.chdir(flask_dir)
    
    env = os.environ.copy()
    env['PYTHONPATH'] = str(flask_dir)
    
    return subprocess.Popen([
        sys.executable, "app.py"
    ], env=env)

def start_fastapi_server():
    """Start the FastAPI server"""
    print("Starting FastAPI server...")
    fastapi_dir = Path(__file__).parent / "fastapi_app"
    os.chdir(fastapi_dir)
    
    env = os.environ.copy()
    env['PYTHONPATH'] = str(fastapi_dir)
    
    return subprocess.Popen([
        sys.executable, "-m", "uvicorn", "main:app", "--reload", "--port", "8000"
    ], env=env)

def main():
    if not check_dependencies():
        sys.exit(1)
    
    print("UBS Coding Challenge 2025 - Server Startup")
    print("=" * 50)
    
    choice = input("Which server would you like to start? (flask/fastapi/both): ").lower()
    
    processes = []
    
    if choice in ["flask", "both"]:
        flask_process = start_flask_server()
        processes.append(("Flask", flask_process))
        time.sleep(2)  # Give Flask time to start
        print("Flask server should be running at: http://localhost:5000")
    
    if choice in ["fastapi", "both"]:
        fastapi_process = start_fastapi_server()
        processes.append(("FastAPI", fastapi_process))
        time.sleep(2)  # Give FastAPI time to start
        print("FastAPI server should be running at: http://localhost:8000")
        print("FastAPI docs available at: http://localhost:8000/docs")
    
    if not processes:
        print("Invalid choice. Please select 'flask', 'fastapi', or 'both'")
        return
    
    print("\nServers are starting up...")
    print("Press Ctrl+C to stop all servers")
    
    try:
        # Wait for all processes
        for name, process in processes:
            process.wait()
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        for name, process in processes:
            print(f"Stopping {name} server...")
            process.terminate()
            process.wait()
        print("All servers stopped.")

if __name__ == "__main__":
    main()
