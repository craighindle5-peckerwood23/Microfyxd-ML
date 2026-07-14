from typing import Dict

def normalize_output(result: Dict[str, any]) -> Dict[str, any]:
    return {
        "intent": result.get("intent", "unknown"),
        "hunter_hits": result.get("hunter_hits", []),
        "score": float(result.get("score", 0.0)),
        "confidence": float(result.get("confidence", 0.0)),
    }
