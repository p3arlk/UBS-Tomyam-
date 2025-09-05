from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
from dotenv import load_dotenv
from models import Challenge, Submission, ChallengeCreate, SubmissionCreate
from routers import challenges, submissions

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="UBS Coding Challenge 2025",
    description="FastAPI server for UBS Coding Challenge",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(challenges.router, prefix="/api/challenges", tags=["challenges"])
app.include_router(submissions.router, prefix="/api/submissions", tags=["submissions"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "UBS Coding Challenge 2025 - FastAPI Server",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "health": "/health",
            "api_challenges": "/api/challenges",
            "api_submissions": "/api/submissions",
            "docs": "/docs",
            "redoc": "/redoc"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "fastapi-server"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=port, 
        reload=True,
        log_level="info"
    )
