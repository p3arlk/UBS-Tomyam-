import pytest
import requests
import json
from datetime import datetime

# Test configuration
FLASK_BASE_URL = "http://localhost:5000"
FASTAPI_BASE_URL = "http://localhost:8000"

class TestFlaskAPI:
    """Tests for Flask API endpoints"""
    
    def test_flask_health_endpoint(self):
        """Test Flask health endpoint"""
        try:
            response = requests.get(f"{FLASK_BASE_URL}/health")
            assert response.status_code == 200
            data = response.json()
            assert data["status"] == "healthy"
            assert "timestamp" in data
        except requests.exceptions.ConnectionError:
            pytest.skip("Flask server not running")
    
    def test_flask_api_challenges(self):
        """Test Flask API challenges endpoint"""
        try:
            response = requests.get(f"{FLASK_BASE_URL}/api/challenges")
            assert response.status_code == 200
            data = response.json()
            assert "challenges" in data
            assert "count" in data
            assert isinstance(data["challenges"], list)
        except requests.exceptions.ConnectionError:
            pytest.skip("Flask server not running")
    
    def test_flask_submit_solution(self):
        """Test Flask solution submission"""
        try:
            payload = {
                "challenge_id": 1,
                "solution": "def two_sum(nums, target): return [0, 1]"
            }
            response = requests.post(
                f"{FLASK_BASE_URL}/api/submit", 
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            assert response.status_code == 201
            data = response.json()
            assert data["status"] == "received"
            assert "submission_id" in data
        except requests.exceptions.ConnectionError:
            pytest.skip("Flask server not running")

class TestFastAPI:
    """Tests for FastAPI endpoints"""
    
    def test_fastapi_health_endpoint(self):
        """Test FastAPI health endpoint"""
        try:
            response = requests.get(f"{FASTAPI_BASE_URL}/health")
            assert response.status_code == 200
            data = response.json()
            assert data["status"] == "healthy"
            assert "timestamp" in data
        except requests.exceptions.ConnectionError:
            pytest.skip("FastAPI server not running")
    
    def test_fastapi_challenges_endpoint(self):
        """Test FastAPI challenges endpoint"""
        try:
            response = requests.get(f"{FASTAPI_BASE_URL}/api/challenges/")
            assert response.status_code == 200
            data = response.json()
            assert "challenges" in data
            assert "total" in data
            assert isinstance(data["challenges"], list)
        except requests.exceptions.ConnectionError:
            pytest.skip("FastAPI server not running")
    
    def test_fastapi_submit_solution(self):
        """Test FastAPI solution submission"""
        try:
            payload = {
                "challenge_id": 1,
                "solution": "def two_sum(nums, target): return [0, 1]"
            }
            response = requests.post(
                f"{FASTAPI_BASE_URL}/api/submissions/", 
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            assert response.status_code == 201
            data = response.json()
            assert "id" in data
            assert data["challenge_id"] == 1
            assert "status" in data
        except requests.exceptions.ConnectionError:
            pytest.skip("FastAPI server not running")
    
    def test_fastapi_docs_accessible(self):
        """Test that FastAPI docs are accessible"""
        try:
            response = requests.get(f"{FASTAPI_BASE_URL}/docs")
            assert response.status_code == 200
        except requests.exceptions.ConnectionError:
            pytest.skip("FastAPI server not running")

class TestDataValidation:
    """Tests for data validation and edge cases"""
    
    def test_invalid_submission_data(self):
        """Test submission with invalid data"""
        try:
            # Test Flask
            payload = {"invalid": "data"}
            response = requests.post(f"{FLASK_BASE_URL}/api/submit", json=payload)
            assert response.status_code == 400
            
            # Test FastAPI
            response = requests.post(f"{FASTAPI_BASE_URL}/api/submissions/", json=payload)
            assert response.status_code == 422  # FastAPI validation error
        except requests.exceptions.ConnectionError:
            pytest.skip("Servers not running")

if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
