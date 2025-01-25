# master/app.py
import sys
import os
import celery
# project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.config import REDIS_URL
from shared.logger import setup_logger
from tasks import process_task

logger = setup_logger("master")

def distribute_tasks():
    # Example tasks
    tasks = ["task1", "task2", "task3", "task4", "task5"]

    # Distribute tasks to workers
    results = []
    for task in tasks:
        logger.info(f"Sending task: {task}")
        result = process_task.delay(task)
        results.append(result)

    # Collect results
    for result in results:
        logger.info(f"Received result: {result.get()}")

if __name__ == "__main__":
    distribute_tasks()