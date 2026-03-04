from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class SeverityLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class ViolationLog(BaseModel):
    candidate_id: str
    timestamp: datetime
    violation_type: str
    severity_level: SeverityLevel
    confidence_score: float
    frame_reference: str