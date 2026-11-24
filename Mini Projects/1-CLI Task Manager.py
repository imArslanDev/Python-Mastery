import json
import os

FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Generate unique task ID
def generate_task_id(tasks):
    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty!")
        return

    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(f"\nID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Status: {status}")

    print("\n================================")


# Update an existing task
def update_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to update: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter new task title: ").strip()

            if not new_title:
                print("Task title cannot be empty!")
                return

            task["title"] = new_title
            save_tasks(tasks)

            print("Task updated successfully!")
            return

    print("Task not found!")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)

            print("Task deleted successfully!")
            return

    print("Task not found!")


# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_id = int(input("\nEnter task ID to complete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task is already completed!")
                return

            task["completed"] = True
            save_tasks(tasks)

            print("Task marked as completed!")
            return

    print("Task not found!")


# Display application menu
def display_menu():
    print("\n================================")
    print("       CLI TASK MANAGER")
    print("================================")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    print("================================")


# Main application
def main():
    tasks = load_tasks()

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            complete_task(tasks)

        elif choice == "6":
            print("\nThank you for using CLI Task Manager!")
            break

        else:
            print("Invalid option! Please select 1-6.")


if __name__ == "__main__":
    main()
