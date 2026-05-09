tasks = []

def add_task():
    task_name = input("Enter the name of the task: ")
    tasks.append(task_name)
    print(f"Task '{task_name}' added successfully!")

def view_tasks():
    try: 
        for x in tasks:
            print(f"- {x}")
    except:
        print("No tasks to display.")

def menu_integration():
    while True:
        print("Welcome to the Task Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Please select an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            menu_integration()
            
menu_integration()