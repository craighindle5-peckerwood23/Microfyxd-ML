from .registry import ModelRegistry

def load_default_models() -> ModelRegistry:
    registry = ModelRegistry()
    registry.register("intent_classifier", object())
    registry.register("scorer", object())
    return registry
