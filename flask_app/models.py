from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Challenge:
    """Data model for coding challenges"""
    id: int
    name: str
    difficulty: str
    points: int
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'difficulty': self.difficulty,
            'points': self.points,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

@dataclass
class Submission:
    """Data model for challenge submissions"""
    id: str
    challenge_id: int
    solution: str
    status: str
    submitted_at: datetime
    score: Optional[int] = None
    
    def to_dict(self):
        return {
            'id': self.id,
            'challenge_id': self.challenge_id,
            'solution': self.solution,
            'status': self.status,
            'submitted_at': self.submitted_at.isoformat(),
            'score': self.score
        }

# Sample data initialization
def get_sample_challenges():
    """Get sample challenges for testing"""
    return [
        Challenge(1, "Two Sum", "Easy", 100, "Find two numbers that add up to target", datetime.now()),
        Challenge(2, "Valid Parentheses", "Medium", 200, "Check if parentheses are valid", datetime.now()),
        Challenge(3, "Merge Sort", "Hard", 300, "Implement merge sort algorithm", datetime.now()),
    ]
