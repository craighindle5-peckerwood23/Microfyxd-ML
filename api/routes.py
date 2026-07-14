from typing import Dict

def health() -> Dict[str, str]:
    return {"status": "ok", "service": "microfyxd-ml"}

def predict_route(body: Dict[str, any]) -> Dict[str, any]:
    from .predict import predict
    return predict(body)
