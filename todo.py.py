def task():
    tasks = []
    print("-------bhai jo bola hai vo krna hai ------")

    total_tasks = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print("Today's tasks are:\n", tasks)

    while True:
        operation = int(input("Enter 1-add\n2-update\n3-delete\n4-view\n5-exit/stop: "))

        if operation == 1:
            add = input("Enter the task you want to do: ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            update_val = input("Enter the task name you want to update: ")
            if update_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Updated task {up}")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Which task do you want to delete: ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
            else:
                print("Task not found.")

        elif operation == 4:
            print("Total tasks:", tasks)

        elif operation == 5:
            print("Closing the program.\nTere baski hai bhai nhi .....")
            break

        else:
            print("Invalid input.")

if __name__ == "__main__":
    task()
