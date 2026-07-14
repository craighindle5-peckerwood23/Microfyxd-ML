from utils.logging import get_logger

logger = get_logger(__name__)


class AudioIngestor:
    def __init__(self, name: str = "audio"):
        self.name = name

    def ingest(self, audio_bytes: bytes) -> dict:
        logger.info("Ingesting audio bytes")
        return {"audio": audio_bytes, "source": self.name}
