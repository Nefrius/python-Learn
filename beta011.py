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
        
def delete_task():
    task_name = input("Enter the name of the task to delete: ")
    if task_name in tasks:
        tasks.remove(task_name)
        print(f"Task '{task_name}' deleted successfully!")
    else:
        print(f"Task '{task_name}' not found.")

def exit_program():
    print("Exiting the Task Manager. Goodbye!")
    exit()

commands = {
    "add": add_task,
    "view": view_tasks,
    "delete": delete_task,
    "exit": exit_program
}

while True:
    choice = input("Please select an option (add/view/delete/exit): ").lower()
    if choice in commands:
        commands[choice]()
    else:
        print("Invalid option. Please try again.")
            


