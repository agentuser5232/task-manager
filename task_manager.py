import json
import os


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                try:
                    self.tasks = json.load(file)
                except json.JSONDecodeError:
                    self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title):
        self.tasks.append({
            "title": title,
            "completed": False
        })
        self.save_tasks()

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            return True
        return False
