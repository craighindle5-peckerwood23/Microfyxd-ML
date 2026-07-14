from utils.logging import get_logger

logger = get_logger(__name__)


def normalize_output(prediction: dict) -> dict:
    logger.info("Normalizing output")
    return {
        "prediction": prediction.get("label"),
        "confidence": prediction.get("confidence"),
    }
