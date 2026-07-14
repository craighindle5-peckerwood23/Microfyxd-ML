from utils.logging import get_logger

logger = get_logger(__name__)


class OCRIngestor:
    def __init__(self, name: str = "ocr"):
        self.name = name

    def ingest(self, image_bytes: bytes) -> dict:
        logger.info("Ingesting OCR image bytes")
        return {"image": image_bytes, "source": self.name}
