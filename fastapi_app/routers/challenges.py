from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models import Challenge, ChallengeCreate, SAMPLE_CHALLENGES, DifficultyLevel
from datetime import datetime

router = APIRouter()

# In-memory storage for development (use database in production)
challenges_db = {challenge.id: challenge for challenge in SAMPLE_CHALLENGES}

@router.get("/", response_model=dict)
async def get_challenges(
    difficulty: Optional[DifficultyLevel] = Query(None, description="Filter by difficulty"),
    limit: int = Query(10, ge=1, le=100, description="Number of challenges to return"),
    offset: int = Query(0, ge=0, description="Number of challenges to skip")
):
    """Get all challenges with optional filtering"""
    all_challenges = list(challenges_db.values())
    
    # Filter by difficulty if specified
    if difficulty:
        all_challenges = [c for c in all_challenges if c.difficulty == difficulty]
    
    # Apply pagination
    total = len(all_challenges)
    challenges = all_challenges[offset:offset + limit]
    
    return {
        "challenges": challenges,
        "total": total,
        "limit": limit,
        "offset": offset,
        "timestamp": datetime.now().isoformat()
    }

@router.get("/{challenge_id}", response_model=Challenge)
async def get_challenge(challenge_id: int):
    """Get a specific challenge by ID"""
    if challenge_id not in challenges_db:
        raise HTTPException(status_code=404, detail="Challenge not found")
    
    return challenges_db[challenge_id]

@router.post("/", response_model=Challenge, status_code=201)
async def create_challenge(challenge: ChallengeCreate):
    """Create a new challenge"""
    # Generate new ID
    new_id = max(challenges_db.keys()) + 1 if challenges_db else 1
    
    new_challenge = Challenge(
        id=new_id,
        name=challenge.name,
        difficulty=challenge.difficulty,
        points=challenge.points,
        description=challenge.description,
        created_at=datetime.now()
    )
    
    challenges_db[new_id] = new_challenge
    return new_challenge

@router.put("/{challenge_id}", response_model=Challenge)
async def update_challenge(challenge_id: int, challenge: ChallengeCreate):
    """Update an existing challenge"""
    if challenge_id not in challenges_db:
        raise HTTPException(status_code=404, detail="Challenge not found")
    
    updated_challenge = Challenge(
        id=challenge_id,
        name=challenge.name,
        difficulty=challenge.difficulty,
        points=challenge.points,
        description=challenge.description,
        created_at=challenges_db[challenge_id].created_at
    )
    
    challenges_db[challenge_id] = updated_challenge
    return updated_challenge

@router.delete("/{challenge_id}")
async def delete_challenge(challenge_id: int):
    """Delete a challenge"""
    if challenge_id not in challenges_db:
        raise HTTPException(status_code=404, detail="Challenge not found")
    
    del challenges_db[challenge_id]
    return {"message": f"Challenge {challenge_id} deleted successfully"}
