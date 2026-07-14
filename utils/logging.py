import logging

logger = logging.getLogger("microfyxd_ml")
logging.basicConfig(level=logging.INFO)

def log_info(msg: str) -> None:
    logger.info(msg)

def log_error(msg: str) -> None:
    logger.error(msg)
