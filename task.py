# Extracting into his own module
from typing import List, Dict
from task_state import TaskState


# Class used to handle everything around the tasks itself, with his own methods to manage them.
class Task:
    def __init__(self):
        self.tasks: List[Dict[str, TaskState]] = []

    # Adds a new task providing a name and a state
    def add_task(self, name: str, state: TaskState):
        self.tasks.append({"name": name, "state": state})

    # Changes the task state of a concrete task, providing the index and the new state
    def change_task_state(self, task_index: int, new_state: TaskState):
        self.tasks[task_index]["state"] = new_state

    # Display the tasks array in a readable format
    def display_tasks(self) -> None:
        if not self.tasks:
            print("No pending tasks.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index}. {task['name']} - {task['state'].value}")

    # Removes a task by his index
    def remove_task(self, task_index: int):
        self.tasks[task_index].pop()
