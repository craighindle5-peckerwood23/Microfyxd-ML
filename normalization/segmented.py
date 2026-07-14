from utils.logging import get_logger

logger = get_logger(__name__)


def segment_text(text: str) -> list:
    logger.info("Segmenting text into sentences (simple split)")
    return [text]
