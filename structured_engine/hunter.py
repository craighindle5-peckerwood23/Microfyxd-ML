from utils.logging import get_logger

logger = get_logger(__name__)


class Hunter:
    def __init__(self, name: str = "default_hunter"):
        self.name = name

    def hunt(self, data: dict) -> dict:
        logger.info("Hunter routing data")
        data["route"] = "default"
        return data
