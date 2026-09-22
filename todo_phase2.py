import json
from datetime import datetime
from pathlib import Path

# Permanent storage file
DATA_FILE = Path("tasks.json")


# -------------------- FILE HANDLING --------------------

def load_tasks():
    """Load tasks from tasks.json."""
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save all tasks permanently to tasks.json."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as error:
        print("Error saving tasks:", error)


# -------------------- INPUT VALIDATION --------------------

def get_task_number(tasks, message="Enter task number: "):
    """Get a valid task number from the user."""
    if not tasks:
        print("No tasks available.")
        return None

    while True:
        try:
            number = int(input(message))
            if 1 <= number <= len(tasks):
                return number - 1
            print(f"Please enter a number from 1 to {len(tasks)}.")
        except ValueError:
            print("Please enter a valid number.")


def get_priority():
    """Get a valid task priority."""
    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
        if priority in ("High", "Medium", "Low"):
            return priority
        print("Invalid priority. Choose High, Medium, or Low.")


def get_due_date(optional=True):
    """Get a valid due date in YYYY-MM-DD format."""
    while True:
        date_text = input(
            "Enter due date (YYYY-MM-DD)"
            + (" or press Enter to skip: " if optional else ": ")
        ).strip()

        if optional and date_text == "":
            return ""

        try:
            due_date = datetime.strptime(date_text, "%Y-%m-%d").date()
            return due_date.isoformat()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, for example 2026-10-15.")


# -------------------- DISPLAY --------------------

def display_tasks(tasks):
    """Display all tasks in a readable format."""
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n" + "=" * 90)
    print(f"{'No.':<5}{'Task':<30}{'Priority':<12}{'Due Date':<15}{'Status':<15}")
    print("=" * 90)

    for i, task in enumerate(tasks, 1):
        task_name = task["task"][:28]
        due_date = task.get("due_date") or "-"
        print(
            f"{i:<5}"
            f"{task_name:<30}"
            f"{task.get('priority', 'Medium'):<12}"
            f"{due_date:<15}"
            f"{task.get('status', 'Pending'):<15}"
        )

    print("=" * 90)


# -------------------- CRUD OPERATIONS --------------------

def add_task(tasks):
    """Create a new task."""
    print("\n--- ADD TASK ---")

    while True:
        task_name = input("Enter task: ").strip()
        if task_name:
            break
        print("Task cannot be empty.")

    priority = get_priority()
    due_date = get_due_date()

    tasks.append({
        "task": task_name,
        "priority": priority,
        "due_date": due_date,
        "status": "Pending"
    })

    save_tasks(tasks)
    print("Task added and saved successfully!")


def view_tasks(tasks):
    """View all tasks."""
    print("\n--- ALL TASKS ---")
    display_tasks(tasks)


def update_task(tasks):
    """Update an existing task."""
    print("\n--- UPDATE TASK ---")
    index = get_task_number(tasks)

    if index is None:
        return

    current = tasks[index]

    print("Press Enter to keep the existing value.")
    print(f"Current task: {current['task']}")
    new_name = input("Enter new task: ").strip()
    if new_name:
        current["task"] = new_name

    print(f"Current priority: {current.get('priority', 'Medium')}")
    change_priority = input("Change priority? (y/n): ").strip().lower()
    if change_priority == "y":
        current["priority"] = get_priority()

    print(f"Current due date: {current.get('due_date') or 'Not set'}")
    change_date = input("Change due date? (y/n): ").strip().lower()
    if change_date == "y":
        current["due_date"] = get_due_date()

    save_tasks(tasks)
    print("Task updated and saved successfully!")


def mark_completed(tasks):
    """Mark a task as completed."""
    print("\n--- MARK AS COMPLETED ---")
    index = get_task_number(tasks)

    if index is None:
        return

    tasks[index]["status"] = "Completed"
    save_tasks(tasks)
    print("Task marked as completed!")


def delete_task(tasks):
    """Delete a task."""
    print("\n--- DELETE TASK ---")
    index = get_task_number(tasks)

    if index is None:
        return

    task_name = tasks[index]["task"]
    confirm = input(f"Delete '{task_name}'? (y/n): ").strip().lower()

    if confirm == "y":
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Delete cancelled.")


# -------------------- OPTIONAL EXTRA FEATURE --------------------

def show_pending_tasks(tasks):
    """Display only pending tasks."""
    pending = [task for task in tasks if task.get("status") == "Pending"]

    print("\n--- PENDING TASKS ---")
    display_tasks(pending)


# -------------------- MAIN MENU --------------------

def main():
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 40)
        print("        PYTHON TO-DO LIST")
        print("=" * 40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark as Completed")
        print("5. Delete Task")
        print("6. View Pending Tasks")
        print("7. Exit")
        print("=" * 40)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 7.")
            continue

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            mark_completed(tasks)
        elif choice == 5:
            delete_task(tasks)
        elif choice == 6:
            show_pending_tasks(tasks)
        elif choice == 7:
            print("Thank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()
