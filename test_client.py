#!/usr/bin/env python3
"""
UBS Coding Challenge 2025 - Flask API Test Client
Test client for the Flask-based coding challenge server
"""

import requests
import json
import time
from datetime import datetime

# Configuration
FLASK_URL = "http://localhost:5000"

def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{title}")
    print("-" * len(title))

def test_server_health():
    """Test server health and basic connectivity"""
    print_section("🏥 Testing Server Health")
    
    try:
        response = requests.get(f"{FLASK_URL}/health", timeout=5)
        print(f"Health Check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Server Status: {data.get('status', 'unknown')}")
            print(f"📅 Timestamp: {data.get('timestamp', 'unknown')}")
            print(f"🏷️  Version: {data.get('version', 'unknown')}")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Flask server is not running!")
        print("   Please start the server with: python flask_app/app.py")
        return False
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_api_overview():
    """Test API overview endpoint"""
    print_section("📋 Testing API Overview")
    
    try:
        response = requests.get(f"{FLASK_URL}/")
        print(f"API Overview: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Message: {data.get('message', '')}")
            print("📍 Available Endpoints:")
            for endpoint, description in data.get('endpoints', {}).items():
                print(f"   • {endpoint}: {description}")
            print("🌟 Features:")
            for feature in data.get('features', []):
                print(f"   • {feature}")
        return True
    except Exception as e:
        print(f"❌ API overview test failed: {e}")
        return False

def test_challenges():
    """Test challenge-related endpoints"""
    print_section("🎯 Testing Challenge Endpoints")
    
    try:
        # Get all challenges
        response = requests.get(f"{FLASK_URL}/api/challenges")
        print(f"Get Challenges: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Found {data['count']} challenges")
            print("📚 Available Challenges:")
            for challenge in data['challenges']:
                print(f"   {challenge['id']}. {challenge['title']} ({challenge['difficulty']}) - {challenge['points']} points")
            
            # Test getting a specific challenge
            if data['challenges']:
                challenge_id = data['challenges'][0]['id']
                response = requests.get(f"{FLASK_URL}/api/challenges/{challenge_id}")
                print(f"\nGet Challenge {challenge_id}: {response.status_code}")
                if response.status_code == 200:
                    challenge = response.json()
                    print(f"✅ Challenge: {challenge['title']}")
                    print(f"📖 Description: {challenge['description'][:100]}...")
                    print(f"🧪 Test Cases: {len(challenge.get('test_cases', []))}")
                    print(f"📊 Stats: {challenge.get('stats', {})}")
        
        return True
    except Exception as e:
        print(f"❌ Challenge test failed: {e}")
        return False

def test_submission():
    """Test solution submission"""
    print_section("📝 Testing Solution Submission")
    
    # Sample solutions for different challenges
    sample_solutions = {
        1: """
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
""",
        2: """
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack
""",
        3: """
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
"""
    }
    
    try:
        # Submit solution for challenge 1 (Two Sum)
        submission_data = {
            "challenge_id": 1,
            "solution": sample_solutions[1],
            "participant_name": "TestUser_" + datetime.now().strftime("%H%M%S")
        }
        
        response = requests.post(f"{FLASK_URL}/api/submit", json=submission_data)
        print(f"Submit Solution: {response.status_code}")
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ Submission ID: {result['submission_id']}")
            print(f"📊 Status: {result['status']}")
            print(f"🎯 Score: {result['score']}/100")
            print(f"📝 Challenge: {result['challenge_title']}")
            
            # Test getting submission details
            submission_id = result['submission_id']
            time.sleep(1)  # Brief delay
            
            response = requests.get(f"{FLASK_URL}/api/submissions/{submission_id}")
            print(f"\nGet Submission: {response.status_code}")
            if response.status_code == 200:
                submission = response.json()
                print(f"✅ Retrieved submission details")
                print(f"🏷️  ID: {submission['id']}")
                print(f"👤 Participant: {submission['participant_name']}")
                print(f"📊 Final Status: {submission['status']}")
                print(f"🎯 Final Score: {submission['score']}")
                
        return True
    except Exception as e:
        print(f"❌ Submission test failed: {e}")
        return False

def test_leaderboard():
    """Test leaderboard functionality"""
    print_section("🏆 Testing Leaderboard")
    
    try:
        response = requests.get(f"{FLASK_URL}/api/leaderboard")
        print(f"Get Leaderboard: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Total Participants: {data['total_participants']}")
            
            if data['leaderboard']:
                print("🏆 Top Participants:")
                for entry in data['leaderboard'][:5]:  # Show top 5
                    print(f"   {entry['rank']}. {entry['participant_name']} - {entry['total_score']} points ({entry['challenges_solved']} solved)")
            else:
                print("📝 No participants yet")
                
        return True
    except Exception as e:
        print(f"❌ Leaderboard test failed: {e}")
        return False

def test_api_status():
    """Test comprehensive API status"""
    print_section("📊 Testing API Status")
    
    try:
        response = requests.get(f"{FLASK_URL}/api/status")
        print(f"Get API Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Service: {data.get('service', 'unknown')}")
            print(f"📊 Statistics:")
            stats = data.get('statistics', {})
            for key, value in stats.items():
                print(f"   • {key.replace('_', ' ').title()}: {value}")
                
        return True
    except Exception as e:
        print(f"❌ API status test failed: {e}")
        return False

def run_complete_test_suite():
    """Run the complete test suite"""
    print_header("UBS Coding Challenge 2025 - Flask API Test Suite")
    print(f"🕐 Test Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Testing Server: {FLASK_URL}")
    
    tests = [
        ("Server Health", test_server_health),
        ("API Overview", test_api_overview),  
        ("Challenges", test_challenges),
        ("Solution Submission", test_submission),
        ("Leaderboard", test_leaderboard),
        ("API Status", test_api_status)
    ]
    
    results = []
    for test_name, test_func in tests:
        print_header(f"Running: {test_name}")
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ Test '{test_name}' crashed: {e}")
            results.append((test_name, False))
        
        time.sleep(0.5)  # Brief pause between tests
    
    # Summary
    print_header("Test Results Summary")
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{status} - {test_name}")
    
    print(f"\n📊 Overall Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your Flask API is working perfectly!")
        print("\n🚀 Next Steps:")
        print("   • Your coding challenge server is ready!")
        print("   • Share the API endpoints with participants")
        print("   • Monitor the leaderboard in real-time")
        print(f"   • Access the server at: {FLASK_URL}")
    else:
        print("⚠️  Some tests failed. Please check the server and try again.")
    
    print(f"\n🕐 Test Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    run_complete_test_suite()
