from utils.logging import get_logger

logger = get_logger(__name__)


class StateTracker:
    def __init__(self):
        self.states = []

    def log_state(self, stage: str, data: dict) -> None:
        logger.info(f"StateTracker logging stage: {stage}")
        self.states.append((stage, data))
