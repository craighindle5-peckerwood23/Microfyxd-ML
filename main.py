from typing import Dict, Any
from api.predict import predict
from api.routes import health

def run_example() -> None:
    print("Health:", health())
    sample: Dict[str, Any] = {"text": "This is a support request with an error."}
    result = predict(sample)
    print("Prediction:", result)

if __name__ == "__main__":
    run_example()
