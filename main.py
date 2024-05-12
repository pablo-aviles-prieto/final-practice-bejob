from task import Task
from task_state import TaskState
from todo_error import TODOError, ErrorType


def main():
    task = Task()
    while True:
        print("\nTODO OPTIONS")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. Display all the tasks")
        print("4. Delete a task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter task name: ")
                task.add_task(name, TaskState.PENDING)

            elif choice == 2:
                task.display_tasks()
                selected_task = int(
                    input("Select the task number to set as completed: ")
                )
                task.change_task_state(selected_task, TaskState.COMPLETED)

            elif choice == 3:
                task.display_tasks()

            elif choice == 4:
                task.display_tasks()
                selected_task = int(input("Select the task number to delete it: "))
                task.remove_task(selected_task)

            elif choice == 5:
                print("\nExiting the program.")
                break

            else:
                raise TODOError.wrong_index(ErrorType.OPTION, choice, 5, 1)

        except TODOError as e:
            print(f"\n{e}")
        # In case the user doesn't provide a valid string number on the input
        except ValueError:
            print("\nPlease enter a valid number.")
        except IndexError as e:
            print(f"\n{e}")


if __name__ == "__main__":
    main()
