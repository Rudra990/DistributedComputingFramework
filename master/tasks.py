from celery import Celery

# Initialize Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_task(data):
    # Simulate task processing
    result = f"Processed: {data}"
    return result