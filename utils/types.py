from typing import TypedDict, List

class PredictionResult(TypedDict):
    intent: str
    hunter_hits: List[str]
    score: float
    confidence: float
