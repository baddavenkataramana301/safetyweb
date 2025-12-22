from pydantic import BaseModel
from typing import List, Dict, Optional

class ControlItem(BaseModel):
    type: str # Hierarchy level
    description: str

class AssessmentResponse(BaseModel):
    risk_score: int
    risk_level: str # Low, Medium, High
    hazards: List[str]
    controls: List[ControlItem]
    confidence: str # Low, Medium, High
    confidence_score: int
    reasoning: Optional[str] = None
    description: Optional[str] = None
    # hira_table: List[Dict] # Can be added for detailed table view
