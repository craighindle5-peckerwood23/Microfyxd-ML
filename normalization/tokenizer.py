from utils.logging import get_logger

logger = get_logger(__name__)


def tokenize(text: str) -> list:
    logger.info("Tokenizing text")
    return text.split()
