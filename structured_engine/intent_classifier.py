from utils.logging import get_logger

logger = get_logger(__name__)


class IntentClassifier:
    def classify_intent(self, text: str) -> str:
        logger.info("Classifying intent (dummy)")
        if "hello" in text.lower():
            return "greeting"
        return "generic"
