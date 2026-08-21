tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append([task, "Pending"])
        print("Task added!")

    elif choice == 2:
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task[0], "-", task[1])

    elif choice == 3:
        n = int(input("Enter task number: "))
        tasks[n-1][0] = input("Enter new task: ")
        print("Task updated!")

    elif choice == 4:
        n = int(input("Enter task number: "))
        tasks[n-1][1] = "Completed"
        print("Task completed!")

    elif choice == 5:
        n = int(input("Enter task number: "))
        tasks.pop(n-1)
        print("Task deleted!")

    elif choice == 6:
        print("Exiting application...")
        break

    else:
        print("Invalid choice!")