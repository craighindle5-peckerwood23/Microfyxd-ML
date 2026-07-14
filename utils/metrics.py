from utils.logging import get_logger

logger = get_logger(__name__)


def log_metric(name: str, value: float) -> None:
    logger.info(f"Metric {name}: {value}")
