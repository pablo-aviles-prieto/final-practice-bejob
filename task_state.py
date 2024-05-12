# Extracting into his own module
from enum import Enum


# Class used to enumerate the possible states of the tasks
class TaskState(Enum):
    TODO = "todo"
    COMPLETED = "completed"
