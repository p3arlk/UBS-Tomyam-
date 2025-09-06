#!/usr/bin/env python3
"""
WSGI entry point for production deployment
"""

import os
import sys

# Add the flask_app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flask_app'))

from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # This is only used when running locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
