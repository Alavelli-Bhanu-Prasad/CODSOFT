tasks = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "3":
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed!")
        else:
            print("Invalid number!")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Wrong choice!")
        