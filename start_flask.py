#!/usr/bin/env python3
"""
UBS Coding Challenge 2025 - Flask Server Startup Script
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask, flask_cors, pytest, requests
        print("✅ All Flask dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def start_flask_server():
    """Start the Flask server"""
    if not check_dependencies():
        return False
    
    print("🚀 Starting UBS Coding Challenge Flask Server...")
    print("=" * 60)
    
    # Change to flask_app directory
    flask_dir = Path(__file__).parent / "flask_app"
    if not flask_dir.exists():
        print("❌ Flask app directory not found!")
        return False
    
    os.chdir(flask_dir)
    
    # Set environment variables
    env = os.environ.copy()
    env['PYTHONPATH'] = str(flask_dir)
    env['FLASK_ENV'] = 'development'
    
    print(f"📁 Working directory: {flask_dir}")
    print(f"🌐 Server will be available at: http://localhost:5000")
    print(f"📋 API endpoints: http://localhost:5000/api/")
    print(f"🏥 Health check: http://localhost:5000/health")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        # Start the Flask server
        result = subprocess.run([
            sys.executable, "app.py"
        ], env=env)
        return result.returncode == 0
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        return True
    except Exception as e:
        print(f"❌ Failed to start Flask server: {e}")
        return False

def main():
    print("UBS Coding Challenge 2025 - Flask Edition")
    print("🏆 Ready for your coding competition!")
    print()
    
    if not start_flask_server():
        print("❌ Failed to start the server")
        sys.exit(1)
    
    print("👋 Server shut down successfully")

if __name__ == "__main__":
    main()
