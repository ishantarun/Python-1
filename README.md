# Simple To-Do List - Project Phase II

## Project Title
**Python-Based To-Do List Application**

## Objective
Develop a simple, interactive Python application to organize and manage daily tasks.

## Phase II Features
- Add/create tasks
- View all tasks
- Update tasks
- Mark tasks as completed
- Delete tasks
- Set task priority: High, Medium, Low
- Set an optional due date
- View pending tasks
- Permanently store tasks using JSON file handling
- Input validation and error handling
- User-friendly command-line menu

## Technologies Used
- Python 3
- JSON file handling
- `datetime`
- `pathlib`

No external libraries are required.

## How to Run

1. Install Python 3.
2. Open a terminal in this project folder.
3. Run:

```bash
python todo_phase2.py
```

A `tasks.json` file is automatically created when the first task is saved.

## Data Storage
Tasks are stored permanently in `tasks.json`.

Example:

```json
[
    {
        "task": "Complete Python project",
        "priority": "High",
        "due_date": "2026-10-15",
        "status": "Pending"
    }
]
```

## Phase I -> Phase II Improvements

| Phase I | Phase II |
|---|---|
| Tasks stored only in memory | Tasks saved permanently in JSON |
| Basic task name and status | Task name, priority, due date and status |
| Limited input validation | Input validation and error handling |
| Basic menu | Expanded user-friendly menu |
| No persistence | Data remains after closing the program |

## Suggested GitHub Collaboration

Use GitHub to demonstrate the 2-mark collaboration component.

Suggested division:
- Member 1: Add task, view task and file-storage functions
- Member 2: Update, complete and delete functions
- Member 3: Input validation, testing and README
- Final merge: test the complete application together

Each member should make commits using their own GitHub account and meaningful commit messages.

Example commit messages:
- `Add JSON file storage`
- `Implement task priority and due date`
- `Add update and delete functions`
- `Add input validation`
- `Update README and testing`

## Viva / Presentation Points

### What is the project?
A command-line Python To-Do List application for creating and managing daily tasks.

### Why JSON?
JSON is simple, human-readable, and allows task data to be stored permanently without requiring an external database.

### What Python concepts are used?
- Variables and data types
- Lists and dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling
- File handling
- JSON serialization
- Date validation

### How does persistence work?
`load_tasks()` reads `tasks.json` when the application starts, and `save_tasks()` writes the updated task list to the file after changes.

### What happens if the user enters invalid input?
The program catches invalid numeric input and validates priority and date formats instead of crashing.

## Testing Checklist

- [ ] Add a task
- [ ] Add a task with High priority
- [ ] Add a task with a due date
- [ ] View tasks
- [ ] Update task name
- [ ] Update priority
- [ ] Update due date
- [ ] Mark a task completed
- [ ] Delete a task
- [ ] View pending tasks
- [ ] Close and reopen the program to verify saved data
- [ ] Test invalid menu input
- [ ] Test invalid task number
- [ ] Test invalid date format
