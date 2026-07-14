from typing import Dict

def score_result(data: Dict[str, any]) -> float:
    hits = len(data.get("hunter_hits", []))
    intent = data.get("intent", "unknown")
    base = 1.0 if intent != "unknown" else 0.5
    return base + hits
