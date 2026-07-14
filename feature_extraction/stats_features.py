from utils.logging import get_logger

logger = get_logger(__name__)


def stats_features(tokens: list) -> dict:
    logger.info("Computing simple stats features")
    length = len(tokens)
    avg_len = sum(len(t) for t in tokens) / length if length > 0 else 0.0
    return {"token_count": length, "avg_token_length": avg_len}
