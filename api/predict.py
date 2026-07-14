from api.ingest import ingest_text
from utils.logging import get_logger

logger = get_logger(__name__)


def run_prediction_demo() -> None:
    sample_text = "Hello world, this is a Microfyxd-ML demo message."
    logger.info("Running prediction demo")
    result = ingest_text(sample_text)
    print("Final result:")
    print(result)
