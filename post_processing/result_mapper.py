from utils.logging import get_logger

logger = get_logger(__name__)


def map_result(normalized: dict, intent: str) -> dict:
    logger.info("Mapping result to final structure")
    return {
        "intent": intent,
        "prediction": normalized.get("prediction"),
        "confidence": normalized.get("confidence"),
    }
