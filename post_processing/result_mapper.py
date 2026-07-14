from typing import Dict

def map_result(data: Dict[str, any]) -> Dict[str, any]:
    return {
        "intent": data.get("intent"),
        "hunter_hits": data.get("hunter_hits", []),
        "score": data.get("score"),
        "confidence": data.get("confidence"),
    }
