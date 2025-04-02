# task_manager.py
import json

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def remove_task(self, task):
        self.tasks = [t for t in self.tasks if t["task"] != task]
        self.save_tasks()

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
        self.save_tasks()

    def list_tasks(self):
        return self.tasks