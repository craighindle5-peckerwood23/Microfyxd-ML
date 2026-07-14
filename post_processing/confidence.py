def compute_confidence(score: float) -> float:
    return max(0.0, min(1.0, score / 5.0))
