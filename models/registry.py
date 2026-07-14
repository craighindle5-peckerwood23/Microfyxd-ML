from typing import Dict, Any
from utils.logging import get_logger

logger = get_logger(__name__)


class ModelRegistry:
    def __init__(self):
        self._models: Dict[str, Any] = {}

    def register(self, name: str, model: Any) -> None:
        logger.info(f"Registering model: {name}")
        self._models[name] = model

    def get(self, name: str) -> Any:
        logger.info(f"Fetching model: {name}")
        return self._models.get(name)
