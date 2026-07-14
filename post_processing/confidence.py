from utils.logging import get_logger

logger = get_logger(__name__)


def adjust_confidence(conf: float, intent: str) -> float:
    logger.info("Adjusting confidence based on intent")
    if intent == "greeting":
        return min(1.0, conf + 0.1)
    return conf
