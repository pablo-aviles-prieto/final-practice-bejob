from task import Task
from task_state import TaskState
from todo_error import TODOError, ErrorType


def main():
    task = Task()
    while True:
        print("\nTODO list")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. Display all the tasks")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                name = input("Enter task name: ")
                task.add_task(name, TaskState.PENDING)

            elif choice == "2":
                task.display_tasks()
                selected_task = int(
                    input("Select the task number to set as completed: ")
                )
                task.change_task_state(selected_task, TaskState.COMPLETED)

            elif choice == "3":
                task.display_tasks()

            elif choice == "4":
                task.display_tasks()
                selected_task = int(input("Select the task number to delete it: "))
                task.remove_task(selected_task)

            elif choice == "5":
                print("Exiting the program.")
                break

            else:
                raise TODOError.wrong_index(ErrorType.OPTION, int(choice), 5)

        except TODOError as e:
            print(e)
        except ValueError:
            print("Please enter a valid number.")
        except IndexError as e:
            print(e)


if __name__ == "__main__":
    main()
