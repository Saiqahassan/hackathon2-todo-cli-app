# Implementation Plan: Python In-Memory Todo CLI

**Branch**: `001-python-todo-cli` | **Date**: 2026-01-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-python-todo-cli/spec.md`

## Summary

The project is to build a Python in-memory Todo CLI application, focusing on five basic features: add, update, delete, view, and mark tasks. The development will be agentic and spec-driven, adhering to the principles outlined in the project constitution.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: `argparse` (from the standard library) for CLI parsing.
**Storage**: In-memory Python dictionary to store the list of tasks.
**Testing**: `pytest` for unit and integration testing.
**Target Platform**: Console / Terminal.
**Project Type**: Single project.
**Performance Goals**: Not applicable for this simple CLI.
**Constraints**: No data persistence, no web frameworks, single-user context.
**Scale/Scope**: The application is designed for a single user and a single, ephemeral session.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ **I. Simplicity and Clarity**: The plan uses Python's standard library (`argparse`) and a simple in-memory dictionary for state, avoiding external dependencies and complex abstractions.
- ✅ **II. Deterministic, In-Memory State**: The entire application state is managed in a single in-memory dictionary, ensuring deterministic behavior as required.
- ✅ **III. Incremental Extensibility**: The proposed structure separates concerns, allowing for future extensions (like different storage backends or UI) with minimal refactoring.
- ✅ **IV. Agent-Friendly and Testable Code**: The code will be organized into modules with clear responsibilities, making it easy to test and for agents to understand and modify.
- ✅ **V. Clean Separation of Concerns**: The plan enforces separation between the core logic (task management service) and the presentation layer (CLI handler).

## Project Structure

### Documentation (this feature)

```text
specs/001-python-todo-cli/
├── plan.md              # This file
├── research.md          # To be created
├── data-model.md        # To be created
├── quickstart.md        # To be created
├── contracts/           # To be created
└── tasks.md             # To be created by /sp.tasks
```

### Source Code (repository root)

```text
# Option 1: Single project (DEFAULT)
src/
├── models/
│   └── task.py          # Defines the Task data structure
├── services/
│   └── todo_service.py  # Core logic for task management
├── cli/
│   └── main.py          # CLI command parsing and execution
└── lib/                   # For any shared utilities (if needed)

tests/
├── integration/
│   └── test_cli.py      # End-to-end tests for CLI commands
└── unit/
    └── test_todo_service.py # Unit tests for the core logic
```

**Structure Decision**: The "Single project" structure is selected. It provides a clean and standard layout that is appropriate for this small-scale application while still separating concerns effectively.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| *None*      | *N/A*        | *N/A*                                 |
