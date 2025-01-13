import json
from task import Task

class TaskFileHandler:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def read_tasks(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_tasks(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as file:
            tasks_data = [task.to_dict() for task in tasks]
            json.dump(tasks_data, file, ensure_ascii=False, indent=2)

