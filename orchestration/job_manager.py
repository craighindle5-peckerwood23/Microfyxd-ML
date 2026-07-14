from utils.logging import get_logger

logger = get_logger(__name__)


class JobManager:
    def __init__(self):
        self.jobs = []

    def submit(self, job_data: dict) -> None:
        logger.info("JobManager submitting job")
        self.jobs.append(job_data)

    def list_jobs(self) -> list:
        return self.jobs
