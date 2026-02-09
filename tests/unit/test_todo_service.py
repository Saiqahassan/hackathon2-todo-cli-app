import pytest
from src.services.todo_service import TodoService
from src.models.task import Task

class TestTodoService:

    @pytest.fixture
    def service(self):
        return TodoService()

    def test_add_task(self, service):
        task = service.add_task("Test task")
        assert task.id == 1
        assert task.description == "Test task"
        assert not task.completed
        assert len(service.get_all_tasks()) == 1

        task2 = service.add_task("Another task")
        assert task2.id == 2
        assert len(service.get_all_tasks()) == 2

    def test_add_task_empty_description_raises_error(self, service):
        with pytest.raises(ValueError, match="Task description cannot be empty."):
            service.add_task("")

    def test_get_all_tasks(self, service):
        assert len(service.get_all_tasks()) == 0
        service.add_task("Task 1")
        service.add_task("Task 2")
        tasks = service.get_all_tasks()
        assert len(tasks) == 2
        assert tasks[0].description == "Task 1"
        assert tasks[1].description == "Task 2"

    def test_get_task_by_id(self, service):
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        
        retrieved_task = service.get_task_by_id(task1.id)
        assert retrieved_task == task1
        
        assert service.get_task_by_id(999) is None

    def test_update_task_description(self, service):
        task = service.add_task("Old description")
        updated_task = service.update_task_description(task.id, "New description")
        
        assert updated_task is not None
        assert updated_task.description == "New description"
        assert service.get_task_by_id(task.id).description == "New description"

        assert service.update_task_description(999, "Non existent") is None

    def test_update_task_description_empty_description_raises_error(self, service):
        task = service.add_task("Old description")
        with pytest.raises(ValueError, match="Task description cannot be empty."):
            service.update_task_description(task.id, "")

    def test_mark_task_complete(self, service):
        task = service.add_task("Incomplete task")
        completed_task = service.mark_task_complete(task.id)
        
        assert completed_task is not None
        assert completed_task.completed
        assert service.get_task_by_id(task.id).completed

        assert service.mark_task_complete(999) is None

    def test_mark_task_incomplete(self, service):
        task = service.add_task("Completed task")
        service.mark_task_complete(task.id) # Mark it complete first
        
        incomplete_task = service.mark_task_incomplete(task.id)
        
        assert incomplete_task is not None
        assert not incomplete_task.completed
        assert not service.get_task_by_id(task.id).completed

        assert service.mark_task_incomplete(999) is None

    def test_delete_task(self, service):
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        
        assert service.delete_task(task1.id)
        assert len(service.get_all_tasks()) == 1
        assert service.get_task_by_id(task1.id) is None

        assert not service.delete_task(999) # Deleting non-existent task
        assert len(service.get_all_tasks()) == 1
