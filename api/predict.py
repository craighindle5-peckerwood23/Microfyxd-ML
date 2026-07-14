from typing import Dict
from orchestration.job_manager import JobManager
from post_processing.confidence import compute_confidence
from post_processing.result_mapper import map_result
from post_processing.output_normalizer import normalize_output
from models.scorer import score_result

_job_manager = JobManager()

def predict(raw: Dict[str, any]) -> Dict[str, any]:
    payload = raw.copy()
    processed = _job_manager.run_job(payload)
    processed["score"] = score_result(processed)
    processed["confidence"] = compute_confidence(processed["score"])
    result = map_result(processed)
    return normalize_output(result)
