from typing import List, Optional
from src.models.task import Task

class TodoService:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, description: str) -> Task:
        if not description:
            raise ValueError("Task description cannot be empty.")
        task = Task(id=self._next_id, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return self._tasks[:] # Return a copy to prevent external modification

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return next((task for task in self._tasks if task.id == task_id), None)

    def update_task_description(self, task_id: int, new_description: str) -> Optional[Task]:
        task = self.get_task_by_id(task_id)
        if task:
            if not new_description:
                raise ValueError("Task description cannot be empty.")
            task.description = new_description
            return task
        return None

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return task
        return None

    def mark_task_incomplete(self, task_id: int) -> Optional[Task]:
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        initial_len = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]
        return len(self._tasks) < initial_len
