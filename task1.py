# TO-DO LIST APPLICATION (Command Line)

tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✓ Completed" if task["completed"] else "✗ Pending"
            print(f"{i}. {task['task']} [{status}]")

def mark_completed():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark completed: "))
        tasks[choice - 1]["completed"] = True
        print("Task marked as completed!")
    except:
        print("Invalid input!")

def update_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to update: "))
        new_task = input("Enter new task name: ")
        tasks[choice - 1]["task"] = new_task
        print("Task updated successfully!")
    except:
        print("Invalid input!")

def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        tasks.pop(choice - 1)
        print("Task deleted successfully!")
    except:
        print("Invalid input!")

# Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        update_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
