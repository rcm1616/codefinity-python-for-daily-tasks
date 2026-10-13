def add_task(tasks, task):
    tasks.append(task) 

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)

def print_tasks(tasks):
    print(tasks)

tasks = []
add_task(tasks, "Buy groceries")
add_task(tasks, "Call the bank")
add_task(tasks, "Walk the dog")
print_tasks(tasks)
remove_task(tasks, "Call the bank")
print_tasks(tasks)
