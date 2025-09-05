#!/usr/bin/env python3
"""
Simple web server to serve the UBS Coding Challenge participant frontend
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

def start_frontend_server(port=8080):
    """Start the frontend web server"""
    
    # Change to web_frontend directory
    frontend_dir = Path(__file__).parent
    os.chdir(frontend_dir)
    
    # Create request handler
    Handler = http.server.SimpleHTTPRequestHandler
    
    # Add CORS headers for API requests
    class CORSRequestHandler(Handler):
        def add_cors_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        
        def do_OPTIONS(self):
            self.send_response(200)
            self.add_cors_headers()
            self.end_headers()
        
        def end_headers(self):
            self.add_cors_headers()
            super().end_headers()
    
    try:
        with socketserver.TCPServer(("", port), CORSRequestHandler) as httpd:
            print("=" * 60)
            print("🌐 UBS Coding Challenge 2025 - Participant Frontend")
            print("=" * 60)
            print(f"📱 Frontend Server: http://localhost:{port}")
            print(f"🚀 Flask API Server: http://localhost:5000")
            print("📁 Serving files from:", os.getcwd())
            print()
            print("📋 Instructions:")
            print("1. Make sure your Flask server is running (python flask_app/app.py)")
            print("2. Open http://localhost:8080 in your web browser")
            print("3. Enter your name and start solving challenges!")
            print()
            print("Press Ctrl+C to stop the server")
            print("=" * 60)
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{port}')
                print(f"🌐 Opening browser automatically...")
            except:
                print(f"💡 Please open http://localhost:{port} in your browser")
            
            print(f"\n🎯 Serving participant frontend on port {port}")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Frontend server stopped")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"   python start_frontend.py {port + 1}")
        else:
            print(f"❌ Failed to start server: {e}")

if __name__ == "__main__":
    import sys
    
    # Allow custom port as command line argument
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8080.")
    
    start_frontend_server(port)
