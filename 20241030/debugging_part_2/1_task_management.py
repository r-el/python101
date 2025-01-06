def add_task(tasks, task_name, status='Pending'):
    tasks[task_name] = {'status': status}

def update_task_status(tasks, task_name, new_status):
    if task_name in tasks:
        tasks[task_name]['status'] = new_status
    else:
        print("Task not found")
    return tasks

def get_pending_tasks(tasks):
    pending_tasks = []
    for task, details in tasks.items():
        if details['status'] == 'Pending':
            pending_tasks.append(task)
    return pending_tasks

tasks = {}
add_task(tasks, "Task 1", "Pending")
add_task(tasks, "Task 2", "Completed")
add_task(tasks, "Task 3", "Pending")
print(get_pending_tasks(tasks))
print(update_task_status(tasks, "Task 4", "Completed"))
print(get_pending_tasks(tasks))