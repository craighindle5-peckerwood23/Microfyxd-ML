from typing import Any, Dict
from structured_engine.engine_parts import EnginePipeline, EnginePart
from structured_engine.hunter import Hunter
from structured_engine.intent_classifier import IntentClassifier

class MLPipeline:
    def __init__(self):
        self.engine = EnginePipeline(parts=[EnginePart("core")])
        self.hunter = Hunter(targets=["error", "warning", "critical"])
        self.intent_classifier = IntentClassifier(labels=["support", "sales", "feedback"])

    def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = self.engine.run(data)
        data = self.hunter.hunt(data)
        data = self.intent_classifier.classify(data)
        return data
