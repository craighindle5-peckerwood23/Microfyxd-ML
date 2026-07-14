from typing import Dict

def vectorize(data: Dict[str, str]) -> Dict[str, float]:
    text = data.get("text", "")
    return {
        "length": float(len(text)),
        "spaces": float(text.count(" ")),
    }
