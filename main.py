from task import Task
from task_state import TaskState
from todo_error import TODOError, ErrorType
from custom_print import CustomPrint


def main():
    task = Task()
    custom_print = CustomPrint()
    custom_print.info("\n###########################")
    custom_print.info("####### TASK MANAGER ######")
    custom_print.info("###########################")
    while True:
        custom_print.header("\nTODO OPTIONS")
        options = [
            "1. Add a task",
            "2. Mark a task as completed",
            f"3. Display all the tasks ({task.total_tasks()})",
            "4. Delete a task",
            "5. Exit",
        ]
        for option in options:
            custom_print.option_list(f"{option}")

        try:
            choice = int(custom_print.input("\nEnter your choice: "))
            if choice == 1:
                name = custom_print.input("Enter task name: ")
                task.add_task(name, TaskState.PENDING)

            elif choice == 2:
                task.display_tasks()
                selected_task = int(
                    custom_print.input("Select the task number to set as completed: ")
                )
                task.change_task_state(selected_task, TaskState.COMPLETED)

            elif choice == 3:
                task.display_tasks()

            elif choice == 4:
                task.display_tasks()
                selected_task = int(
                    custom_print.input("Select the task number to delete it: ")
                )
                task.remove_task(selected_task)

            elif choice == 5:
                custom_print.info("\nExiting the program.\n")
                break

            else:
                raise TODOError.wrong_index(ErrorType.OPTION, choice, 5, 1)

        except TODOError as e:
            custom_print.error(f"\n{e}")
        # In case the user doesn't provide a valid string number on the input
        except ValueError:
            custom_print.error("\nPlease enter a valid number.")
        except IndexError as e:
            custom_print.error(f"\n{e}")


if __name__ == "__main__":
    main()
