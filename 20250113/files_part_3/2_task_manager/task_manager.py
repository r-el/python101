from task import Task
from task_file_handler import TaskFileHandler

class TaskManager:
    def __init__(self):
        self.file_handler = TaskFileHandler()
        self.tasks = self.file_handler.read_tasks()

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.file_handler.save_tasks(self.tasks)
        return task

    def get_all_tasks(self):
        return self.tasks

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.file_handler.save_tasks(self.tasks)
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.file_handler.save_tasks(self.tasks)
            return True
        return False
