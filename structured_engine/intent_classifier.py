from typing import Any, Dict

class IntentClassifier:
    def __init__(self, labels: list[str]):
        self.labels = labels

    def classify(self, data: Dict[str, Any]) -> Dict[str, Any]:
        text = str(data.get("text", "")).lower()
        intent = "unknown"
        for label in self.labels:
            if label in text:
                intent = label
                break
        data["intent"] = intent
        return data
