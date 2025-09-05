from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class DifficultyLevel(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class SubmissionStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    ERROR = "error"

# Pydantic models for FastAPI
class ChallengeBase(BaseModel):
    name: str = Field(..., description="Name of the challenge")
    difficulty: DifficultyLevel = Field(..., description="Difficulty level")
    points: int = Field(..., gt=0, description="Points awarded for solving")
    description: Optional[str] = Field(None, description="Challenge description")

class ChallengeCreate(ChallengeBase):
    pass

class Challenge(ChallengeBase):
    id: int = Field(..., description="Unique challenge identifier")
    created_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        from_attributes = True

class SubmissionBase(BaseModel):
    challenge_id: int = Field(..., description="ID of the challenge being solved")
    solution: str = Field(..., description="Solution code")

class SubmissionCreate(SubmissionBase):
    pass

class Submission(SubmissionBase):
    id: str = Field(..., description="Unique submission identifier")
    status: SubmissionStatus = Field(default=SubmissionStatus.PENDING)
    submitted_at: datetime = Field(default_factory=datetime.now)
    score: Optional[int] = Field(None, ge=0, le=100, description="Score percentage")
    
    class Config:
        from_attributes = True

class APIResponse(BaseModel):
    message: str
    timestamp: datetime = Field(default_factory=datetime.now)
    data: Optional[dict] = None

# Sample data for development
SAMPLE_CHALLENGES = [
    Challenge(
        id=1,
        name="Two Sum",
        difficulty=DifficultyLevel.EASY,
        points=100,
        description="Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
        created_at=datetime.now()
    ),
    Challenge(
        id=2,
        name="Valid Parentheses",
        difficulty=DifficultyLevel.MEDIUM,
        points=200,
        description="Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        created_at=datetime.now()
    ),
    Challenge(
        id=3,
        name="Merge Sort Implementation",
        difficulty=DifficultyLevel.HARD,
        points=300,
        description="Implement the merge sort algorithm to sort an array of integers.",
        created_at=datetime.now()
    )
]
