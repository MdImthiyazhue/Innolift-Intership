# Day 4 - Task 3
# To-Do List Manager

# List to store tasks
tasks = [
    "Complete Python assignment",
    "Attend internship",
    "Practice Data Structures"
]


# Function to add a new task
def add_task(task):
    tasks.append(task)
    print(f'"{task}" has been added.')


# Function to complete (remove) a task
def complete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'"{task}" has been completed and removed.')
    else:
        print(f'"{task}" not found.')


# Function to return the number of pending tasks
def pending_count():
    return len(tasks)


# Display all pending tasks
def list_tasks():
    print("\n===== TO-DO LIST =====")
    if not tasks:
        print("No pending tasks.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


# -------------------------
# Program Execution
# -------------------------

list_tasks()

add_task("Review Day 4 tasks")

complete_task("Attend internship")

list_tasks()

print(f"\nPending Tasks: {pending_count()}")