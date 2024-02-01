import time

class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        print("Timer started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Timer stopped. Elapsed time: {elapsed_time} seconds")

# Usage
with TimerContext():
    # Code inside this block will be timed
    time.sleep(2)  # Simulating some processing time


class Task:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing task: {self.name}")
        # Simulating some task execution
        time.sleep(3)

# Define a convenient API for the Task class
class ConvenientTaskAPI:
    def __init__(self, task_name):
        self.task = Task(task_name)

    def run_with_timing(self):
        with TimerContext():
            self.task.execute()

# Usage
convenient_task = ConvenientTaskAPI("Sample Task")
convenient_task.run_with_timing()
