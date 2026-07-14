from utils.logging import get_logger

logger = get_logger(__name__)


class EnginePart:
    def __init__(self, name: str):
        self.name = name

    def process(self, data: dict) -> dict:
        logger.info(f"EnginePart {self.name} processing data")
        return data
