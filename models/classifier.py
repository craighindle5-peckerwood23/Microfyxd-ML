from typing import Dict

def classify(features: Dict[str, float]) -> str:
    length = features.get("length", 0.0)
    if length < 20:
        return "short"
    elif length < 100:
        return "medium"
    return "long"
