# Extracting everythiong involving the errors into his own module
from enum import Enum


# Class used to enumerate the possible type of errors to display in the CLI
class ErrorType(Enum):
    TASK = "task"
    OPTION = "option"


class TODOError(Exception):
    """Handles all error logic for the todo list and tasks.
    Uses static methods, allowing access without class instantiation.
    """

    @staticmethod
    def duplicated_task(task_name: str):
        # Raise an error indicating the duplicated task
        return TODOError(f"ERROR! Task '{task_name}' already exists.")

    @staticmethod
    def wrong_index(type_retrieved: ErrorType, task_index: int, max_index: int):
        """Return an error indicating an index out of range
        and whats the type being retrieved"""
        if max_index < 0:
            return IndexError(f"ERROR! No {type_retrieved.value}s available.")
        elif max_index == 0:
            return IndexError(
                f"ERROR! There is only one {type_retrieved.value} available. Valid index: 0."
            )
        else:
            return IndexError(
                f"ERROR! Index '{task_index}' is out of range. Valid {type_retrieved.value} indices: 0 to {max_index}."
            )
