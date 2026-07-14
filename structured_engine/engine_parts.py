from typing import Any, Dict

class EnginePart:
    def __init__(self, name: str):
        self.name = name

    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return data

class EnginePipeline:
    def __init__(self, parts: list[EnginePart]):
        self.parts = parts

    def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        for part in self.parts:
            data = part.process(data)
        return data
