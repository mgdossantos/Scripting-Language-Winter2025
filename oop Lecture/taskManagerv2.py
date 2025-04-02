class TaskManager:
    def __init__(self, name):
        self.name = name  # Initializing the 'name' attribute
        self.tasks = []  # Initializing the 'tasks' attribute as an empty list

    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})

    def remove_task(self, description):
        self.tasks = [t for t in self.tasks if t["description"] != description]

    def list_tasks(self):
        return self.tasks