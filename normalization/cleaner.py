import re
from utils.logging import get_logger

logger = get_logger(__name__)


def clean_text(text: str) -> str:
    logger.info("Cleaning text")
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
