from flask import Blueprint, jsonify, request
from datetime import datetime
import json

# Create API blueprint
api_bp = Blueprint('api', __name__)

# Sample data for demonstration
sample_data = [
    {'id': 1, 'name': 'Challenge 1', 'difficulty': 'Easy', 'points': 100},
    {'id': 2, 'name': 'Challenge 2', 'difficulty': 'Medium', 'points': 200},
    {'id': 3, 'name': 'Challenge 3', 'difficulty': 'Hard', 'points': 300},
]

@api_bp.route('/')
def api_home():
    return jsonify({
        'message': 'UBS Coding Challenge API',
        'version': '1.0',
        'endpoints': {
            'challenges': '/challenges',
            'challenges_by_id': '/challenges/<id>',
            'submit': '/submit',
            'status': '/status'
        }
    })

@api_bp.route('/challenges', methods=['GET'])
def get_challenges():
    """Get all challenges"""
    return jsonify({
        'challenges': sample_data,
        'count': len(sample_data),
        'timestamp': datetime.now().isoformat()
    })

@api_bp.route('/challenges/<int:challenge_id>', methods=['GET'])
def get_challenge(challenge_id):
    """Get a specific challenge by ID"""
    challenge = next((c for c in sample_data if c['id'] == challenge_id), None)
    if challenge:
        return jsonify(challenge)
    return jsonify({'error': 'Challenge not found'}), 404

@api_bp.route('/submit', methods=['POST'])
def submit_solution():
    """Submit a solution"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    required_fields = ['challenge_id', 'solution']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields: challenge_id, solution'}), 400
    
    # Here you would typically validate and process the solution
    response = {
        'status': 'received',
        'challenge_id': data['challenge_id'],
        'submission_id': f"sub_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        'timestamp': datetime.now().isoformat(),
        'message': 'Solution submitted successfully'
    }
    
    return jsonify(response), 201

@api_bp.route('/status', methods=['GET'])
def get_status():
    """Get API status"""
    return jsonify({
        'status': 'operational',
        'uptime': 'Unknown',  # You could track this
        'total_challenges': len(sample_data),
        'timestamp': datetime.now().isoformat()
    })
