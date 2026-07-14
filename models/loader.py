from models.registry import ModelRegistry
from models.classifier import RuleBasedClassifier
from utils.logging import get_logger

logger = get_logger(__name__)


def load_models() -> ModelRegistry:
    logger.info("Loading models into registry")
    registry = ModelRegistry()
    registry.register("rule_classifier", RuleBasedClassifier())
    return registry
