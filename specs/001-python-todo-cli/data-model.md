# Data Model: Todo Application

## Entity: Task

Represents a single todo item in the list.

### Fields

- **`id`** (integer): A unique, auto-incrementing identifier for the task. This will be managed by the `TodoService`.
- **`description`** (string): The text content of the task. This is provided by the user.
- **`completed`** (boolean): The status of the task.
  - `false`: The task is incomplete (default).
  - `true`: The task is complete.

### Relationships

- A `Task` entity is self-contained and has no direct relationships with other entities. The collection of tasks is managed by the `TodoService`.

### State Transitions

A `Task` object can transition between the following states:

- **Creation**: A task is created with an `id`, a `description`, and a `completed` status of `false`.
- **Update**: The `description` of a task can be modified.
- **Completion**: The `completed` status can be toggled between `true` and `false`.
- **Deletion**: A task can be removed from the system.

### Validation Rules

- The `description` field must not be empty.
