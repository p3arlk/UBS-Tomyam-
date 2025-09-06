from flask import Blueprint, jsonify, request
from datetime import datetime
import json
import requests
import logging

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
            'status': '/status',
            'external_apis': {
                'jsonplaceholder': '/external/jsonplaceholder',
                'httpbin': '/external/httpbin',
                'weather': '/external/weather?city=<city_name>',
                'custom_request': '/external/custom (POST)'
            }
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

# External API Endpoints
# ==========================================
# This section contains endpoints that make requests to external websites/APIs
# Add your external website integrations here following the patterns below

@api_bp.route('/external/jsonplaceholder', methods=['GET'])
def get_jsonplaceholder_posts():
    """
    EXAMPLE: Fetch posts from JSONPlaceholder API
    
    TO ADD YOUR OWN EXTERNAL WEBSITE:
    1. Copy this function structure
    2. Replace the URL with your target website
    3. Update the response processing logic
    4. Add appropriate error handling
    """
    try:
        # STEP 1: Make the external API call
        # Replace this URL with your external website's API endpoint
        response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=10)
        response.raise_for_status()
        
        # STEP 2: Process the response
        # Modify this section based on your external website's response format
        posts = response.json()
        # Limit to first 10 posts for demo
        limited_posts = posts[:10]
        
        # STEP 3: Return formatted response to your frontend
        # Customize this return structure based on what your frontend needs
        return jsonify({
            'status': 'success',
            'source': 'jsonplaceholder.typicode.com',
            'total_posts': len(posts),
            'returned_posts': len(limited_posts),
            'posts': limited_posts,
            'timestamp': datetime.now().isoformat()
        })
        
    except requests.exceptions.RequestException as e:
        # STEP 4: Handle errors gracefully
        logging.error(f"JSONPlaceholder API error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Failed to fetch from JSONPlaceholder API: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500

@api_bp.route('/external/httpbin', methods=['GET'])
def get_httpbin_data():
    """Fetch data from HTTPBin API"""
    try:
        response = requests.get('https://httpbin.org/json', timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        return jsonify({
            'status': 'success',
            'source': 'httpbin.org',
            'data': data,
            'timestamp': datetime.now().isoformat()
        })
        
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTPBin API error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Failed to fetch from HTTPBin API: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500

@api_bp.route('/external/weather', methods=['GET'])
def get_weather_demo():
    """
    EXAMPLE: Weather API Integration Template
    
    TO INTEGRATE A REAL WEATHER API:
    1. Sign up for a weather service (OpenWeatherMap, WeatherAPI, etc.)
    2. Get your API key
    3. Replace the mock data section with actual API call
    4. Update the response processing
    """
    try:
        # Get city parameter from request
        city = request.args.get('city', 'London')
        
        # REPLACE THIS SECTION WITH REAL WEATHER API CALL
        # Example for OpenWeatherMap:
        # api_key = os.getenv('OPENWEATHER_API_KEY')  # Add this to your .env file
        # url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        # response = requests.get(url, timeout=10)
        # response.raise_for_status()
        # weather_data = response.json()
        
        # FOR NOW: Using mock data for demo
        mock_weather_data = {
            'city': city,
            'temperature': '22°C',
            'description': 'Partly cloudy',
            'humidity': '65%',
            'wind_speed': '10 km/h',
            'demo_note': 'This is mock data. Replace with actual weather API call.'
        }
        
        return jsonify({
            'status': 'success',
            'source': 'weather-api-demo',
            'weather': mock_weather_data,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logging.error(f"Weather API error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Failed to fetch weather data: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500

@api_bp.route('/external/custom', methods=['POST'])
def make_custom_request():
    """Make a custom request to any external API"""
    try:
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({
                'status': 'error',
                'message': 'URL is required in request body'
            }), 400
        
        url = data['url']
        method = data.get('method', 'GET').upper()
        headers = data.get('headers', {})
        params = data.get('params', {})
        body = data.get('body', {})
        
        # Security: Only allow certain domains for safety
        allowed_domains = [
            'jsonplaceholder.typicode.com',
            'httpbin.org',
            'api.github.com',
            'reqres.in'
        ]
        
        domain_allowed = any(domain in url for domain in allowed_domains)
        if not domain_allowed:
            return jsonify({
                'status': 'error',
                'message': 'Domain not in allowed list for security reasons',
                'allowed_domains': allowed_domains
            }), 403
        
        # Make the request
        if method == 'GET':
            response = requests.get(url, headers=headers, params=params, timeout=10)
        elif method == 'POST':
            response = requests.post(url, headers=headers, params=params, json=body, timeout=10)
        else:
            return jsonify({
                'status': 'error',
                'message': f'HTTP method {method} not supported'
            }), 400
        
        response.raise_for_status()
        
        # Try to parse as JSON, fallback to text
        try:
            response_data = response.json()
        except:
            response_data = response.text
        
        return jsonify({
            'status': 'success',
            'request_url': url,
            'request_method': method,
            'response_status': response.status_code,
            'response_data': response_data,
            'timestamp': datetime.now().isoformat()
        })
        
    except requests.exceptions.RequestException as e:
        logging.error(f"Custom request error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Request failed: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Unexpected error: {str(e)}',
            'timestamp': datetime.now().isoformat()
        }), 500

# ==========================================
# TEMPLATE FUNCTIONS FOR EXTERNAL WEBSITES
# ==========================================
# Copy and modify these templates to add your own external website integrations

# Template 1: Simple GET request to external API
# @api_bp.route('/external/your-api-name', methods=['GET'])
# def get_your_api_data():
#     """
#     Template for integrating a simple external API
#     
#     STEPS TO CUSTOMIZE:
#     1. Replace 'your-api-name' in the route with your API name
#     2. Replace the function name 'get_your_api_data'
#     3. Update the URL in the requests.get() call
#     4. Modify the response processing logic
#     """
#     try:
#         # STEP 1: Make the API call
#         response = requests.get('https://your-external-website.com/api/endpoint', timeout=10)
#         response.raise_for_status()
#         
#         # STEP 2: Process the response
#         data = response.json()  # or response.text for non-JSON APIs
#         
#         # STEP 3: Return processed data
#         return jsonify({
#             'status': 'success',
#             'source': 'your-external-website.com',
#             'data': data,
#             'timestamp': datetime.now().isoformat()
#         })
#         
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Your API error: {e}")
#         return jsonify({
#             'status': 'error',
#             'message': f'Failed to fetch from your API: {str(e)}',
#             'timestamp': datetime.now().isoformat()
#         }), 500

# Template 2: API with authentication (API key)
# @api_bp.route('/external/api-with-auth', methods=['GET'])
# def get_authenticated_api_data():
#     """
#     Template for APIs that require authentication
#     
#     STEPS TO CUSTOMIZE:
#     1. Add your API key to .env file: YOUR_API_KEY=your_actual_key
#     2. Update the URL and headers
#     3. Modify the response processing
#     """
#     try:
#         # Get API key from environment variables
#         # api_key = os.getenv('YOUR_API_KEY')
#         # if not api_key:
#         #     return jsonify({'status': 'error', 'message': 'API key not configured'}), 500
#         
#         # Headers with authentication
#         # headers = {
#         #     'Authorization': f'Bearer {api_key}',  # or 'X-API-Key': api_key
#         #     'Content-Type': 'application/json'
#         # }
#         
#         # Make authenticated request
#         # response = requests.get('https://api.example.com/data', headers=headers, timeout=10)
#         # response.raise_for_status()
#         
#         # return jsonify({
#         #     'status': 'success',
#         #     'data': response.json(),
#         #     'timestamp': datetime.now().isoformat()
#         # })
#         
#         # Placeholder return
#         return jsonify({'status': 'template', 'message': 'Uncomment and customize this function'})
#         
#     except Exception as e:
#         logging.error(f"Authenticated API error: {e}")
#         return jsonify({
#             'status': 'error',
#             'message': f'Authentication API error: {str(e)}',
#             'timestamp': datetime.now().isoformat()
#         }), 500

# Template 3: POST request to external API
# @api_bp.route('/external/post-to-api', methods=['POST'])
# def post_to_external_api():
#     """
#     Template for sending data to external APIs
#     
#     STEPS TO CUSTOMIZE:
#     1. Update the external API URL
#     2. Modify the data processing
#     3. Update the request payload structure
#     """
#     try:
#         # Get data from your frontend
#         # frontend_data = request.get_json()
#         
#         # Prepare data for external API
#         # payload = {
#         #     'field1': frontend_data.get('field1'),
#         #     'field2': frontend_data.get('field2'),
#         #     # Add more fields as needed
#         # }
#         
#         # Send POST request to external API
#         # response = requests.post(
#         #     'https://external-api.com/submit',
#         #     json=payload,
#         #     headers={'Content-Type': 'application/json'},
#         #     timeout=10
#         # )
#         # response.raise_for_status()
#         
#         # return jsonify({
#         #     'status': 'success',
#         #     'external_response': response.json(),
#         #     'timestamp': datetime.now().isoformat()
#         # })
#         
#         # Placeholder return
#         return jsonify({'status': 'template', 'message': 'Uncomment and customize this function'})
#         
#     except Exception as e:
#         logging.error(f"POST API error: {e}")
#         return jsonify({
#             'status': 'error',
#             'message': f'POST request failed: {str(e)}',
#             'timestamp': datetime.now().isoformat()
#         }), 500

# ==========================================
# POPULAR EXTERNAL APIS TO INTEGRATE
# ==========================================
# Here are some popular external APIs you might want to integrate:
#
# 1. NEWS APIs:
#    - NewsAPI: https://newsapi.org/
#    - Guardian API: https://open-platform.theguardian.com/
#
# 2. SOCIAL MEDIA APIs:
#    - Twitter API: https://developer.twitter.com/
#    - Reddit API: https://www.reddit.com/dev/api/
#
# 3. FINANCE APIs:
#    - Alpha Vantage: https://www.alphavantage.co/
#    - Yahoo Finance: https://rapidapi.com/apidojo/api/yahoo-finance1/
#
# 4. WEATHER APIs:
#    - OpenWeatherMap: https://openweathermap.org/api
#    - WeatherAPI: https://www.weatherapi.com/
#
# 5. MAPS & LOCATION:
#    - Google Maps API: https://developers.google.com/maps
#    - MapBox: https://docs.mapbox.com/api/
#
# 6. ENTERTAINMENT:
#    - TMDB (Movies): https://www.themoviedb.org/documentation/api
#    - Spotify API: https://developer.spotify.com/
#
# 7. GOVERNMENT DATA:
#    - US Government APIs: https://api.data.gov/
#    - World Bank API: https://datahelpdesk.worldbank.org/knowledgebase/articles/889392
#
# IMPORTANT NOTES:
# - Always check API rate limits and terms of service
# - Store API keys in environment variables (.env file)
# - Add proper error handling for network timeouts
# - Consider caching responses for better performance
