# Define a list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. [{status}] {task['task']}")

# Function to mark a task as completed
def mark_task_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main loop
while True:
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")