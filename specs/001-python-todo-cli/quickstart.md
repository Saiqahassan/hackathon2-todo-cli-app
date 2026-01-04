# Quickstart: Python Todo CLI

This document explains how to set up and run the Python Todo CLI application.

## Prerequisites

- Python 3.11 or higher.

## Setup

There are no external dependencies to install. The application uses only the Python standard library.

## Running the Application

The application is run from the root of the project directory using the `python -m` command to execute the main CLI module.

### Command Structure

```bash
python -m src.cli.main <command> [arguments]
```

### Available Commands

- `add <description>`: Adds a new task.
- `list`: Shows all tasks.
- `update <id> <new_description>`: Updates a task's description.
- `complete <id>`: Marks a task as complete.
- `uncomplete <id>`: Marks a task as incomplete.
- `delete <id>`: Deletes a task.

### Examples

**Adding a task:**
```bash
python -m src.cli.main add "Buy groceries"
```

**Listing tasks:**
```bash
python -m src.cli.main list
```

**Marking a task as complete:**
```bash
python -m src.cli.main complete 1
```

**Deleting a task:**
```bash
python -m src.cli.main delete 2
```
