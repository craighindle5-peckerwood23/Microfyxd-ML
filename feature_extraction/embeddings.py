from utils.logging import get_logger

logger = get_logger(__name__)


def dummy_embeddings(tokens: list) -> dict:
    logger.info("Creating dummy embeddings")
    return {token: float(len(token)) for token in tokens}
