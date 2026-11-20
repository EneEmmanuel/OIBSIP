tasks = []

while True:
    print("=== MY TO DO LIST ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. EXIT")

    choice = input("1-4: ")

    if choice == "1":
        new_task = input("Enter your task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
           print("no task found")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice =="3":
        if len(tasks) == 0:
            print("no task to delete! ")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                num = int(input("which number you want to delete"))
                tasks.pop(num - 1)
                print("task deleted!")

    elif choice == "4":
        print("good bye")
        break
