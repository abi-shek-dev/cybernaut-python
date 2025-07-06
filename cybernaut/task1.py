
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task by Index")
        print("4. Mark Task as Completed")
        print("5. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            index = int(input("Enter index to remove: "))
            if 0 <= index < len(tasks):
                tasks.pop(index)
            else:
                print("Invalid index.")
        elif choice == "4":
            index = int(input("Enter index to mark as completed: "))
            if 0 <= index < len(tasks):
                tasks[index] += " ✅"
            else:
                print("Invalid index.")
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
