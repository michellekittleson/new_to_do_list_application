tasks = []

def add_task():
    task = input("Enter the task you would like to add: ")
    tasks.append(task)
    print(f"\n{task} added to the To Do List! ")

def view_tasks():
    print("\nTo Do List: ")
    for task in tasks:
        print(task)

def mark_complete():
    completed_task = input("Enter the task to mark complete: ")
    if completed_task in tasks:
        print(f"\n{completed_task} marked complete! ")
        tasks.remove(completed_task)
    else:
        print(f"\n{completed_task} not found in To Do List. ")

def delete_task():
    deleted_task = input("Enter task to delete: ")
    if deleted_task in tasks:
        print(f"\n{deleted_task} deleted from To Do List. ")
        tasks.remove(deleted_task)
    else:
        print(f"\n{deleted_task} not found in To Do List.")

def main():
    while True:
        print("\nMenu:\n1. Add a task\n2. View tasks\n3. Mark a task as complete\n4. Delete a task\n5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Thank you for using the To Do List App!")
            break
        else:
            print("Please enter a valid choice: (1, 2, 3, 4, or 5): ")

main()