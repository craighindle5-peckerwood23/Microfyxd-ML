from typing import Dict, Any

class ModelRegistry:
    def __init__(self):
        self._models: Dict[str, Any] = {}

    def register(self, name: str, model: Any) -> None:
        self._models[name] = model

    def get(self, name: str) -> Any:
        return self._models.get(name)
