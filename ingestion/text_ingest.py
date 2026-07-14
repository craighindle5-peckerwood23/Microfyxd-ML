from utils.logging import get_logger

logger = get_logger(__name__)


class TextIngestor:
    def __init__(self, name: str = "text"):
        self.name = name

    def ingest(self, text: str) -> dict:
        logger.info("Ingesting text")
        return {"text": text, "source": self.name}
