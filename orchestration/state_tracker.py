from typing import Any, Dict

class StateTracker:
    def __init__(self):
        self._states: Dict[str, Dict[str, Any]] = {}

    def set_state(self, job_id: str, state: Dict[str, Any]) -> None:
        self._states[job_id] = state

    def get_state(self, job_id: str) -> Dict[str, Any]:
        return self._states.get(job_id, {})
