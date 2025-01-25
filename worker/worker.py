from celery import Celery

# Initialize Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_task(data):
    # Simulate task processing
    result = f"Processed: {data}"
    return result

if __name__ == "__main__":
    # Start the worker
    app.worker_main(argv=["worker", "--loglevel=info"])