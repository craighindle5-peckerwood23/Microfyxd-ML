from typing import Any, Dict

class Hunter:
    def __init__(self, targets: list[str]):
        self.targets = targets

    def hunt(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data["hunter_hits"] = [t for t in self.targets if t in str(data)]
        return data
