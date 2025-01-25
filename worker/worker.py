# worker/worker.py
import sys
import os

# project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from celery import Celery
from shared.config import REDIS_URL
from shared.logger import setup_logger

logger = setup_logger("worker")

# Initialize Celery app
app = Celery('tasks', broker=REDIS_URL)

@app.task
def process_task(data):
    logger.info(f"Processing task: {data}")
    # Simulate task processing
    result = f"Processed: {data}"
    return result

if __name__ == "__main__":
    # Start the worker
    app.worker_main(argv=["worker", "--loglevel=info"])