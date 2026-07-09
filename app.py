from task_manager import TaskManager


def display_menu():
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")


def main():
    manager = TaskManager()

    while True:
        display_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":
            tasks = manager.list_tasks()

            if not tasks:
                print("No tasks available.")
                continue

            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i}. {task['title']} [{status}]")

        elif choice == "2":
            title = input("Task title: ").strip()

            if title:
                manager.add_task(title)
                print("Task added.")
            else:
                print("Task title cannot be empty.")

        elif choice == "3":
            try:
                task_number = int(input("Task number: "))

                if manager.complete_task(task_number - 1):
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
