from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models import Submission, SubmissionCreate, SubmissionStatus
from datetime import datetime
import uuid

router = APIRouter()

# In-memory storage for development (use database in production)
submissions_db = {}

@router.get("/", response_model=dict)
async def get_submissions(
    challenge_id: Optional[int] = Query(None, description="Filter by challenge ID"),
    status: Optional[SubmissionStatus] = Query(None, description="Filter by status"),
    limit: int = Query(10, ge=1, le=100, description="Number of submissions to return"),
    offset: int = Query(0, ge=0, description="Number of submissions to skip")
):
    """Get all submissions with optional filtering"""
    all_submissions = list(submissions_db.values())
    
    # Filter by challenge_id if specified
    if challenge_id:
        all_submissions = [s for s in all_submissions if s.challenge_id == challenge_id]
    
    # Filter by status if specified
    if status:
        all_submissions = [s for s in all_submissions if s.status == status]
    
    # Apply pagination
    total = len(all_submissions)
    submissions = all_submissions[offset:offset + limit]
    
    return {
        "submissions": submissions,
        "total": total,
        "limit": limit,
        "offset": offset,
        "timestamp": datetime.now().isoformat()
    }

@router.get("/{submission_id}", response_model=Submission)
async def get_submission(submission_id: str):
    """Get a specific submission by ID"""
    if submission_id not in submissions_db:
        raise HTTPException(status_code=404, detail="Submission not found")
    
    return submissions_db[submission_id]

@router.post("/", response_model=Submission, status_code=201)
async def create_submission(submission: SubmissionCreate):
    """Submit a solution for a challenge"""
    # Generate unique submission ID
    submission_id = f"sub_{uuid.uuid4().hex[:8]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    new_submission = Submission(
        id=submission_id,
        challenge_id=submission.challenge_id,
        solution=submission.solution,
        status=SubmissionStatus.PENDING,
        submitted_at=datetime.now()
    )
    
    # Here you would typically:
    # 1. Validate the solution
    # 2. Run tests against the solution
    # 3. Calculate score
    # For now, we'll simulate this with a simple check
    
    # Simulate processing delay and scoring
    if len(submission.solution.strip()) > 10:  # Basic validation
        new_submission.status = SubmissionStatus.ACCEPTED
        new_submission.score = 85  # Simulated score
    else:
        new_submission.status = SubmissionStatus.REJECTED
        new_submission.score = 0
    
    submissions_db[submission_id] = new_submission
    return new_submission

@router.put("/{submission_id}/status", response_model=Submission)
async def update_submission_status(
    submission_id: str, 
    status: SubmissionStatus,
    score: Optional[int] = Query(None, ge=0, le=100, description="Score percentage")
):
    """Update submission status and score"""
    if submission_id not in submissions_db:
        raise HTTPException(status_code=404, detail="Submission not found")
    
    submission = submissions_db[submission_id]
    submission.status = status
    if score is not None:
        submission.score = score
    
    return submission

@router.delete("/{submission_id}")
async def delete_submission(submission_id: str):
    """Delete a submission"""
    if submission_id not in submissions_db:
        raise HTTPException(status_code=404, detail="Submission not found")
    
    del submissions_db[submission_id]
    return {"message": f"Submission {submission_id} deleted successfully"}
