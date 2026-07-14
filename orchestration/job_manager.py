from typing import Any, Dict
from .pipeline import MLPipeline

class JobManager:
    def __init__(self):
        self.pipeline = MLPipeline()

    def run_job(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.pipeline.run(payload)
