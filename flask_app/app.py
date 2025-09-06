from flask import Flask, jsonify, request
from flask.logging import create_logger
from flask_cors import CORS
import os
from dotenv import load_dotenv
from datetime import datetime
from routes import api_bp

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for all routes
    CORS(app)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Basic routes
    @app.route('/')
    def home():
        return jsonify({
            'message': '67 Tomyam UBS Coding Challenge 2025 Flask Server',
            'timestamp': datetime.now().isoformat(),
            'endpoints': {
                'health': '/health',
                'api': '/api/',
                'docs': 'No built-in docs (consider FastAPI for auto-docs)'
            }
        })
    
    @app.route('/health')
    def health():
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'service': 'flask-server'
        })
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    logger = create_logger(app)
    logger.info('Starting Flask application...')
    
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
