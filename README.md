# UBS Coding Challenge 2025 🚀

A comprehensive **Flask-based** web server for coding challenges, featuring complete API endpoints, real-time scoring, leaderboard tracking, and automated solution validation.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

## ✨ Features

- 🏆 **Complete Coding Challenge Platform**: End-to-end pipeline for competitive programming
- 🧪 **Automated Solution Validation**: Real-time code testing and scoring
- 📊 **Live Leaderboard**: Real-time participant rankings and statistics  
- 🎯 **Challenge Management**: Pre-built coding challenges with test cases
- 🔒 **Production Ready**: Environment configuration and security considerations
- 🏥 **Health Monitoring**: Built-in monitoring and status endpoints
- 🌐 **CORS Support**: Cross-origin request handling for web frontends
- 📝 **Comprehensive API**: RESTful endpoints for all challenge operations

## 🎯 Perfect For
- **Coding Competitions & Hackathons**
- **Technical Interviews & Assessments** 
- **Programming Bootcamps & Education**
- **Corporate Training & Team Building**

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ubs-coding-challenge-2025.git
cd ubs-coding-challenge-2025
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

4. **Start the server**

**Option A: Windows Batch Script**
```bash
# Double-click start_flask.bat
```

**Option B: Python Script**
```bash
python start_flask.py
```

**Option C: Manual Start**
```bash
cd flask_app
python app.py
```

🌐 **Server runs at:** http://localhost:5000

## 🌐 API Endpoints

### Core Endpoints
- `GET /` - Welcome message and API overview
- `GET /health` - Health check and system status
- `GET /api/` - API information and statistics

### Challenge Management
- `GET /api/challenges` - List all challenges (with filtering)
- `GET /api/challenges/<id>` - Get detailed challenge information
- Filter by difficulty: `/api/challenges?difficulty=Easy`

### Solution Submission & Tracking
- `POST /api/submit` - Submit solution for validation
- `GET /api/submissions/<id>` - Get submission details and status

### Leaderboard & Statistics
- `GET /api/leaderboard` - Current participant rankings
- `GET /api/status` - Comprehensive API statistics

## 🧪 Testing

### Run the comprehensive test client
```bash
python test_client.py
```

### Run unit tests
```bash
pytest tests/ -v
```

### Test API endpoints manually
```bash
# Health check
curl http://localhost:5000/health

# Get challenges
curl http://localhost:5000/api/challenges

# Submit solution
curl -X POST http://localhost:5000/api/submit \
  -H "Content-Type: application/json" \
  -d '{
    "challenge_id": 1,
    "solution": "def two_sum(nums, target): return [0, 1]",
    "participant_name": "YourName"
  }'
```

## 📊 Sample Challenges Included

1. **Two Sum** (Easy - 100 pts)
   - Classic array problem with hash map optimization
   - Tests algorithmic thinking and optimization

2. **Valid Parentheses** (Medium - 200 pts)  
   - Stack-based string validation problem
   - Tests data structure knowledge

3. **Merge Sorted Arrays** (Hard - 300 pts)
   - In-place array merging with two pointers
   - Tests advanced array manipulation

## 🏆 Scoring System

- **Automatic Code Validation**: Syntax checking and basic logic validation
- **Intelligent Scoring**: Points awarded based on solution quality and approach
- **Real-time Feedback**: Immediate status updates (accepted/rejected/partial)
- **Leaderboard Integration**: Automatic ranking updates

## 🎯 Usage Examples

### Submit a Solution
```python
import requests

solution_data = {
    "challenge_id": 1,
    "participant_name": "Alice",
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
    "http://localhost:5000/api/submit",
    json=solution_data
)
print(response.json())
```

### Check Leaderboard
```python
response = requests.get("http://localhost:5000/api/leaderboard")
leaderboard = response.json()

for participant in leaderboard['leaderboard']:
    print(f"{participant['rank']}. {participant['participant_name']} - {participant['total_score']} points")
```

## 🛠 Customization

### Adding New Challenges
Edit `flask_app/routes.py` and add to `SAMPLE_CHALLENGES`:

```python
{
    'id': 4,
    'title': 'Your Challenge',
    'difficulty': 'Medium',
    'points': 200,
    'description': 'Your challenge description...',
    'test_cases': [
        {'input': {'param': 'value'}, 'expected': 'result'}
    ]
}
```

### Custom Scoring Logic
Modify the `validate_solution()` function in `routes.py` to implement your scoring algorithm.

### Database Integration
- Uncomment SQLAlchemy in `requirements.txt`
- Replace in-memory storage with database models
- Update connection string in `.env`

## 🐳 Docker Deployment

```bash
# Build and run
docker build -t ubs-challenge .
docker run -p 5000:5000 ubs-challenge

# Or use Docker Compose
docker-compose up flask-app
```

## ⚙️ Configuration

### Environment Variables (.env)
```bash
DEBUG=True
SECRET_KEY=your-secure-secret-key
PORT=5000
ALLOWED_ORIGINS=*
```

## 📁 Project Structure

```
├── flask_app/              # Main Flask application
│   ├── app.py             # Flask app configuration
│   ├── routes.py          # API endpoints and logic
│   └── models.py          # Data models
├── tests/                 # Test suite
├── start_flask.py         # Python startup script
├── start_flask.bat        # Windows startup script  
├── test_client.py         # API testing client
├── requirements.txt       # Flask-specific dependencies
├── .env.template         # Environment configuration
└── README.md             # This file
```

## � Production Deployment

1. **Set production environment**:
   ```bash
   export FLASK_ENV=production
   export DEBUG=False
   ```

2. **Use production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 flask_app.app:app
   ```

3. **Configure reverse proxy** (nginx/Apache)

4. **Set up SSL certificates**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Why Flask?

- **Simplicity**: Easy to understand and extend
- **Reliability**: Battle-tested framework with excellent documentation
- **Flexibility**: Perfect for coding challenges and rapid prototyping
- **Performance**: Lightweight and fast for competition scenarios
- **Community**: Large ecosystem and extensive third-party support

## 🆘 Support

- 📖 Check the comprehensive test client: `python test_client.py`
- 🐛 Report issues on GitHub
- 💡 Contribute improvements and new features

---

**Ready to run your coding challenge?** 🏆

Start the server and begin coding! 🚀

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ubs-coding-challenge-2025.git
cd ubs-coding-challenge-2025
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
