# CLI Contracts: Todo Application

This document defines the command-line interface for the Todo application. The application will be invoked as `python -m src.cli.main`.

## Commands

### `add`

Adds a new task to the todo list.

- **Usage**: `python -m src.cli.main add <description>`
- **Arguments**:
  - `description` (string, required): The description of the task to add. Must be enclosed in quotes if it contains spaces.
- **Success Output**: "Task added."
- **Error Output**: "Error: Description cannot be empty."

### `list`

Displays all tasks in the todo list.

- **Usage**: `python -m src.cli.main list`
- **Arguments**: None.
- **Success Output**: A formatted list of tasks, e.g.:
  ```
  ID  Status      Description
  --  ----------  ----------------
  1   [ ]         Buy milk
  2   [X]         Walk the dog
  ```
- **Empty List Output**: "Your todo list is empty!"

### `update`

Updates the description of an existing task.

- **Usage**: `python -m src.cli.main update <id> <new_description>`
- **Arguments**:
  - `id` (integer, required): The ID of the task to update.
  - `new_description` (string, required): The new description for the task.
- **Success Output**: "Task <id> updated."
- **Error Output**: "Error: Task not found."

### `complete`

Marks a task as complete.

- **Usage**: `python -m src.cli.main complete <id>`
- **Arguments**:
  - `id` (integer, required): The ID of the task to mark as complete.
- **Success Output**: "Task <id> marked as complete."
- **Error Output**: "Error: Task not found."

### `uncomplete`

Marks a task as incomplete.

- **Usage**: `python -m src.cli.main uncomplete <id>`
- **Arguments**:
  - `id` (integer, required): The ID of the task to mark as incomplete.
- **Success Output**: "Task <id> marked as incomplete."
- **Error Output**: "Error: Task not found."

### `delete`

Deletes a task from the todo list.

- **Usage**: `python -m src.cli.main delete <id>`
- **Arguments**:
  - `id` (integer, required): The ID of the task to delete.
- **Success Output**: "Task <id> deleted."
- **Error Output**: "Error: Task not found."
