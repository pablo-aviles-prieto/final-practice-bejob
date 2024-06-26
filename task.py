# Extracting the task class into his own module
from typing import List, Dict
from task_state import TaskState
from todo_error import TODOError, ErrorType
from custom_print import CustomPrint


# Handles everything around the tasks itself, with his own methods to manage them.
class Task:
    def __init__(self):
        self.tasks: List[Dict[str, TaskState]] = []
        self.custom_print = CustomPrint()

    # Adds a new task providing a name and a state
    def add_task(self, name: str, state: TaskState):
        # Throwing exception when the name of the task is duplicated
        if any(task["name"] == name for task in self.tasks):
            raise TODOError.duplicated_task(name)
        self.tasks.append({"name": name, "state": state.value})
        self.custom_print.success(f"\nTask '{name}' ({state.value}) successfully added.")

    # Changes the task state, providing the index and the new state
    def change_task_state(self, task_index: int, new_state: TaskState):
        self.validate_task_index(task_index)
        self.tasks[task_index]["state"] = new_state.value
        self.custom_print.success(f"\nTask '{self.tasks[task_index]["name"]}' changed his state to '{new_state.value}' successfully.")

    # Display the tasks array in a readable format
    def display_tasks(self) -> None:
        if not self.tasks:
            raise TODOError.no_tasks()
        else:
            self.custom_print.header("\nTask list", self.custom_print.BLUE)
            for index, task in enumerate(self.tasks):
                state_upper = f"[{task['state']}]".upper()
                self.custom_print.info(f"{index}. {task['name']} {state_upper}")

    # Removes a task by his index
    def remove_task(self, task_index: int):
        self.validate_task_index(task_index)
        task_name = self.tasks[task_index]["name"]  # Get the task name before removing it
        self.tasks.pop(task_index)
        self.custom_print.success(f"\nTask '{task_name}' successfully deleted.")

    # Validate the task index and raise an error if it's out of range.
    def validate_task_index(self, task_index: int):
        max_task_index = len(self.tasks) - 1
        if task_index < 0 or task_index > max_task_index:
            raise TODOError.wrong_index(ErrorType.TASK, task_index, max_task_index)

    def total_tasks(self):
        return len(self.tasks)
