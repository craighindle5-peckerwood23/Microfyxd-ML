from orchestration.pipeline import Pipeline
from utils.logging import get_logger

logger = get_logger(__name__)


def ingest_text(text: str) -> dict:
    logger.info("API ingest_text called")
    pipeline = Pipeline()
    result = pipeline.run({"text": text})
    return result
