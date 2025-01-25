from tasks import process_task

def distribute_tasks():
    # Example tasks
    tasks = ["task1", "task2", "task3", "task4", "task5"]

    # Distribute tasks to workers
    results = []
    for task in tasks:
        result = process_task.delay(task)
        results.append(result)

    # Collect results
    for result in results:
        print(result.get())

if __name__ == "__main__":
    distribute_tasks()