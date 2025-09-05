#!/usr/bin/env python3
"""
Sample client script to test the UBS Coding Challenge APIs
"""

import requests
import json
import time
from datetime import datetime

# Configuration
FLASK_URL = "http://localhost:5000"
FASTAPI_URL = "http://localhost:8000"

def test_flask_api():
    """Test Flask API endpoints"""
    print("Testing Flask API...")
    print("-" * 30)
    
    try:
        # Test health endpoint
        response = requests.get(f"{FLASK_URL}/health")
        print(f"Health check: {response.status_code}")
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
        
        # Test challenges endpoint
        response = requests.get(f"{FLASK_URL}/api/challenges")
        print(f"\nChallenges: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Found {data['count']} challenges")
            for challenge in data['challenges']:
                print(f"  - {challenge['name']} ({challenge['difficulty']}) - {challenge['points']} points")
        
        # Test submission
        submission_data = {
            "challenge_id": 1,
            "solution": """
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
"""
        }
        
        response = requests.post(f"{FLASK_URL}/api/submit", json=submission_data)
        print(f"\nSubmission: {response.status_code}")
        if response.status_code == 201:
            print(json.dumps(response.json(), indent=2))
            
    except requests.exceptions.ConnectionError:
        print("❌ Flask server is not running")
    except Exception as e:
        print(f"❌ Error testing Flask API: {e}")

def test_fastapi():
    """Test FastAPI endpoints"""
    print("\nTesting FastAPI...")
    print("-" * 30)
    
    try:
        # Test health endpoint
        response = requests.get(f"{FASTAPI_URL}/health")
        print(f"Health check: {response.status_code}")
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2))
        
        # Test challenges endpoint
        response = requests.get(f"{FASTAPI_URL}/api/challenges/")
        print(f"\nChallenges: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Found {data['total']} challenges")
            for challenge in data['challenges']:
                print(f"  - {challenge['name']} ({challenge['difficulty']}) - {challenge['points']} points")
        
        # Test submission
        submission_data = {
            "challenge_id": 1,
            "solution": """
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
"""
        }
        
        response = requests.post(f"{FASTAPI_URL}/api/submissions/", json=submission_data)
        print(f"\nSubmission: {response.status_code}")
        if response.status_code == 201:
            submission_result = response.json()
            print(json.dumps(submission_result, indent=2))
            
            # Test getting the submission back
            submission_id = submission_result['id']
            response = requests.get(f"{FASTAPI_URL}/api/submissions/{submission_id}")
            print(f"\nGet submission: {response.status_code}")
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=2))
            
    except requests.exceptions.ConnectionError:
        print("❌ FastAPI server is not running")
    except Exception as e:
        print(f"❌ Error testing FastAPI: {e}")

def main():
    print("UBS Coding Challenge 2025 - API Test Client")
    print("=" * 50)
    print(f"Timestamp: {datetime.now().isoformat()}")
    
    # Test both APIs
    test_flask_api()
    test_fastapi()
    
    print("\n" + "=" * 50)
    print("Testing complete!")
    print("\nAPI Documentation:")
    print(f"Flask API: {FLASK_URL}/")
    print(f"FastAPI Docs: {FASTAPI_URL}/docs")
    print(f"FastAPI ReDoc: {FASTAPI_URL}/redoc")

if __name__ == "__main__":
    main()
