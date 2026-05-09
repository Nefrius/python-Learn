tasks = []

for i in range(3):
    task_name = input(f"Enter name for task {i+1}: ")
    tasks.append(task_name)

print("\nYour Tasks:")
for idx, task in enumerate(tasks, start=1):
    print(f"{idx}. {task}")
