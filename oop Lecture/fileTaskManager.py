from taskManagerv3 import *
import json

class FileTaskManager(TaskManager):
    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []