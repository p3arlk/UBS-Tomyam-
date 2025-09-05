# UBS Coding Challenge 2025 🚀

A comprehensive web server template for coding challenges, featuring both **Flask** and **FastAPI** implementations with complete API endpoints, testing, and deployment configurations.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)
![FastAPI](https://img.shields.io/badge/fastapi-0.104.1-teal.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- 🐍 **Dual Framework Support**: Choose between Flask (simple) or FastAPI (advanced)
- 📚 **Auto-Generated Documentation**: Interactive API docs with FastAPI
- 🧪 **Complete Testing Suite**: Unit tests and integration tests included
- 🐳 **Docker Ready**: Containerized deployment with Docker Compose
- 🔒 **Production Ready**: Environment configuration and security considerations
- 🎯 **Challenge Management**: CRUD operations for coding challenges
- 📝 **Solution Submission**: Handle and validate code submissions
- 🏥 **Health Monitoring**: Built-in health check endpoints

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/p3arlk/UBS-Tomyam-.git
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.template .env
# Edit .env with your configuration
```

4. **Start the servers**

**Option A: Windows Batch Script**
```bash
# Double-click start_servers.bat and choose your option
```

**Option B: Python Script**
```bash
python start_servers.py
```

**Option C: Manual Start**

Flask Server:
```bash
cd flask_app
python app.py
```

FastAPI Server:
```bash
cd fastapi_app
uvicorn main:app --reload --port 8000
```

## 🌐 API Endpoints

### Flask API (Port 5000)
- `GET /` - Welcome message and endpoint overview
- `GET /health` - Health check
- `GET /api/challenges` - List all challenges
- `GET /api/challenges/<id>` - Get specific challenge
- `POST /api/submit` - Submit a solution

### FastAPI API (Port 8000)
- `GET /` - Welcome message and endpoint overview
- `GET /health` - Health check
- `GET /api/challenges/` - List challenges (with filtering & pagination)
- `GET /api/challenges/{id}` - Get specific challenge
- `POST /api/challenges/` - Create new challenge
- `PUT /api/challenges/{id}` - Update challenge
- `DELETE /api/challenges/{id}` - Delete challenge
- `GET /api/submissions/` - List submissions (with filtering)
- `POST /api/submissions/` - Submit solution
- `GET /api/submissions/{id}` - Get specific submission
- `PUT /api/submissions/{id}/status` - Update submission status

### 📖 Documentation
- **FastAPI Interactive Docs**: http://localhost:8000/docs
- **FastAPI ReDoc**: http://localhost:8000/redoc

## 🧪 Testing

### Run the test client
```bash
python test_client.py
```

### Run unit tests
```bash
pytest tests/ -v
```

### Test API endpoints manually
```bash
# Test Flask health
curl http://localhost:5000/health

# Test FastAPI health  
curl http://localhost:8000/health

# Get challenges
curl http://localhost:8000/api/challenges/

# Submit solution
curl -X POST http://localhost:8000/api/submissions/ \
  -H "Content-Type: application/json" \
  -d '{"challenge_id": 1, "solution": "def solution(): return True"}'
```

## 🐳 Docker Deployment

### Using Docker Compose
```bash
# Start both services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down
```

### Individual Docker Build
```bash
# Build image
docker build -t ubs-challenge .

# Run Flask container
docker run -p 5000:5000 -e FLASK_APP=flask_app/app.py ubs-challenge

# Run FastAPI container
docker run -p 8000:8000 ubs-challenge uvicorn fastapi_app.main:app --host 0.0.0.0
```

## 📁 Project Structure

```
├── flask_app/              # Flask implementation
│   ├── app.py             # Main Flask application
│   ├── routes.py          # API route definitions
│   └── models.py          # Data models
├── fastapi_app/           # FastAPI implementation
│   ├── main.py            # Main FastAPI application
│   ├── models.py          # Pydantic models & schemas
│   └── routers/           # Modular route definitions
│       ├── challenges.py  # Challenge-related endpoints
│       └── submissions.py # Submission-related endpoints
├── tests/                 # Test suite
│   ├── __init__.py       
│   └── test_api.py        # API integration tests
├── .env.template          # Environment variables template
├── .gitignore            # Git ignore rules
├── requirements.txt       # Python dependencies
├── start_servers.bat      # Windows batch script
├── start_servers.py       # Cross-platform Python script
├── test_client.py         # API testing client
├── Dockerfile            # Docker container definition
├── docker-compose.yml     # Multi-service Docker setup
└── README.md             # This file
```

## ⚙️ Configuration

### Environment Variables

Copy `.env.template` to `.env` and configure:

```bash
# Server Configuration
DEBUG=True
SECRET_KEY=your-secure-secret-key
PORT=5000
FASTAPI_PORT=8000

# Database (optional)
DATABASE_URL=sqlite:///./challenge.db

# CORS (production)
ALLOWED_ORIGINS=https://yourdomain.com
```

## 🎯 Usage Examples

### Creating a Challenge (FastAPI)
```python
import requests

challenge_data = {
    "name": "Two Sum Problem",
    "difficulty": "Easy", 
    "points": 100,
    "description": "Find two numbers that add up to target"
}

response = requests.post(
    "http://localhost:8000/api/challenges/",
    json=challenge_data
)
print(response.json())
```

### Submitting a Solution
```python
solution_data = {
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

response = requests.post(
    "http://localhost:8000/api/submissions/",
    json=solution_data  
)
print(response.json())
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for the UBS Coding Challenge 2025
- Flask and FastAPI communities for excellent documentation
- Contributors and testers

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/ubs-coding-challenge-2025/issues) page
2. Create a new issue with detailed information
3. Check the API documentation at `/docs` (FastAPI)

---

**Happy Coding!** 🎉
