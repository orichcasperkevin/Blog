from abc import ABC,abstractmethod
import time


class TaskADT(ABC):
    @abstractmethod
    def execute():
        pass

class Task(TaskADT):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing task: {self.name}")
        # Simulating some task execution
        time.sleep(3)

# Define a convenient API for the Task class
        
class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        print("Timer started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Timer stopped. Elapsed time: {elapsed_time} seconds")


class TimedTask(TaskADT):
    def __init__(self, task_instance: TaskADT):
        self.task = task_instance

    def execute(self):
        with TimerContext():
            self.task.execute()

# Usage
task_instance = Task("Sample Task")
timed_task = TimedTask(task_instance)
timed_task.execute()
