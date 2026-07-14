from typing import Dict

def build_stats_features(data: Dict[str, str]) -> Dict[str, float]:
    text = data.get("text", "")
    return {
        "uppercase_ratio": float(sum(c.isupper() for c in text)) / max(len(text), 1),
        "digit_ratio": float(sum(c.isdigit() for c in text)) / max(len(text), 1),
    }
