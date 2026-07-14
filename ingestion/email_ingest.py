from utils.logging import get_logger

logger = get_logger(__name__)


class EmailIngestor:
    def __init__(self, name: str = "email"):
        self.name = name

    def ingest(self, subject: str, body: str) -> dict:
        logger.info("Ingesting email")
        return {"subject": subject, "body": body, "source": self.name}
