from utils.logging import get_logger

logger = get_logger(__name__)


def score_prediction(prediction: dict) -> dict:
    logger.info("Scoring prediction")
    label = prediction.get("label", "unknown")
    confidence = 0.5
    if label == "empty":
        confidence = 0.9
    elif label == "short":
        confidence = 0.7
    elif label == "long":
        confidence = 0.8
    return {"label": label, "confidence": confidence}
