tasks = []

def add_task():
    task = input("Enter a task: ")
    if task.strip() != "":
        tasks.append({"task": task, "completed": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i + 1}. [{status}] {task['task']}")

def mark_complete():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
