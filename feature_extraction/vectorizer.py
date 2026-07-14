from collections import Counter
from utils.logging import get_logger

logger = get_logger(__name__)


def bow_vector(tokens: list) -> dict:
    logger.info("Creating bag-of-words vector")
    return dict(Counter(tokens))
