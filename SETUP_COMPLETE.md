# UBS Coding Challenge 2025

### 📁 Project Structure
```
UBS Coding Challenge 2025/
├── flask_app/                 # Flask web server
│   ├── app.py                # Main Flask application
│   ├── routes.py             # API routes
│   └── models.py             # Data models
├── fastapi_app/              # FastAPI web server
│   ├── main.py               # Main FastAPI application
│   ├── models.py             # Pydantic models
│   └── routers/              # API route modules
│       ├── challenges.py     # Challenge endpoints
│       └── submissions.py    # Submission endpoints
├── tests/                    # Test files
│   └── test_api.py          # API integration tests
├── requirements.txt          # Python dependencies
├── .env                     # Environment variables
├── start_servers.bat        # Windows batch script to start servers
├── start_servers.py         # Python script to start servers
├── test_client.py           # Sample client to test APIs
├── Dockerfile               # Docker container setup
├── docker-compose.yml       # Multi-container setup
└── README.md               # Documentation
```

## 🚀 Quick Start

### Option 1: Use the Windows Batch Script
Double-click `start_servers.bat` and choose:
1. Flask Server (port 5000)
2. FastAPI Server (port 8000)  
3. Both servers

### Option 2: Manual Start

#### Flask Server:
```bash
cd flask_app
python app.py
```
📍 Access at: http://localhost:5000

#### FastAPI Server:
```bash
cd fastapi_app
uvicorn main:app --reload --port 8000
```
📍 Access at: http://localhost:8000
📍 Interactive docs: http://localhost:8000/docs

### Option 3: Docker (if you have Docker installed)
```bash
docker-compose up
```

## 🛠 API Endpoints

### Flask API (Port 5000)
- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/challenges` - Get all challenges
- `GET /api/challenges/<id>` - Get specific challenge
- `POST /api/submit` - Submit solution

### FastAPI API (Port 8000)
- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/challenges/` - Get all challenges (with filtering)
- `GET /api/challenges/{id}` - Get specific challenge
- `POST /api/challenges/` - Create new challenge
- `GET /api/submissions/` - Get all submissions
- `POST /api/submissions/` - Submit solution
- `GET /docs` - Interactive API documentation

## 🧪 Testing

### Run the test client:
```bash
python test_client.py
```

### Run unit tests:
```bash
pytest tests/
```

## 💡 Features

### Flask Server:
- ✅ RESTful API endpoints
- ✅ JSON responses
- ✅ Error handling
- ✅ Environment configuration
- ✅ Blueprint structure

### FastAPI Server:
- ✅ RESTful API endpoints
- ✅ Automatic API documentation
- ✅ Data validation with Pydantic
- ✅ Type hints
- ✅ Query parameters and filtering
- ✅ CORS support
- ✅ Status code handling

### Both Servers Include:
- ✅ Health check endpoints
- ✅ Challenge management
- ✅ Solution submission
- ✅ Sample data for testing
- ✅ Proper error responses
- ✅ Timestamp tracking

## 🔧 Customization

### Adding New Challenges:
- **Flask**: Modify `sample_data` in `flask_app/routes.py`
- **FastAPI**: Modify `SAMPLE_CHALLENGES` in `fastapi_app/models.py`

### Adding Database:
- Uncomment SQLAlchemy in requirements.txt
- Configure DATABASE_URL in .env
- Implement database models

### Adding Authentication:
- Add JWT token handling
- Implement user registration/login
- Secure sensitive endpoints

## 🎯 Next Steps

1. **Choose your preferred framework** (Flask for simplicity, FastAPI for advanced features)
2. **Customize the challenge data** to match your contest requirements
3. **Add business logic** for solution validation and scoring
4. **Implement database storage** for persistence
5. **Add authentication** if needed
6. **Deploy to cloud** when ready

## 🌟 Recommendations

- **For beginners**: Start with Flask - it's simpler and more straightforward
- **For advanced features**: Use FastAPI - automatic docs, better validation, async support

