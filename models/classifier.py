from utils.logging import get_logger

logger = get_logger(__name__)


class RuleBasedClassifier:
    def predict(self, features: dict) -> dict:
        logger.info("Running rule-based classifier")
        token_count = features.get("stats", {}).get("token_count", 0)
        if token_count == 0:
            label = "empty"
        elif token_count < 5:
            label = "short"
        else:
            label = "long"
        return {"label": label}
