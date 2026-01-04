# Tasks: Python In-Memory Todo CLI

**Input**: Design documents from `specs/001-python-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project root `src/` directory
- [X] T002 Create `src/models/` directory
- [X] T003 Create `src/services/` directory
- [X] T004 Create `src/cli/` directory
- [X] T005 Create `tests/` directory
- [X] T006 Create `tests/unit/` directory
- [X] T007 Create `tests/integration/` directory
- [X] T008 [P] Configure `pytest` setup (e.g. create `pytest.ini` if needed, although usually not necessary for basic setup)

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T009 Define `Task` class in `src/models/task.py` (id, description, completed: bool)
- [X] T010 Implement `TodoService` class in `src/services/todo_service.py` with methods for:
    - Adding tasks (generates unique IDs)
    - Retrieving all tasks
    - Retrieving a single task by ID
    - Updating task description
    - Marking task as complete/incomplete
    - Deleting tasks
- [X] T011 Implement unit tests for `TodoService` in `tests/unit/test_todo_service.py` to cover all service methods.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

## Phase 3: User Story 1 - Add a new task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks to their in-memory todo list.

**Independent Test**: Execute the `add` command, then the `list` command to verify the task appears.

### Implementation for User Story 1

- [X] T012 [US1] Implement `add` command parsing and execution logic in `src/cli/main.py` using `argparse`. This will call the `TodoService.add_task` method.
- [X] T013 [US1] Implement integration tests for the `add` command in `tests/integration/test_cli.py`, verifying task creation and output.

## Phase 4: User Story 2 - View the list of tasks (Priority: P1)

**Goal**: Allow users to view all tasks currently in their todo list.

**Independent Test**: Execute the `list` command and verify all tasks (including their status) are displayed correctly.

### Implementation for User Story 2

- [ ] T014 [US2] Implement `list` command parsing and execution logic in `src/cli/main.py`. This will call `TodoService.get_all_tasks` and format the output.
- [ ] T015 [US2] Implement integration tests for the `list` command in `tests/integration/test_cli.py`, covering empty list and multiple tasks scenarios.

## Phase 5: User Story 3 - Update an existing task (Priority: P2)

**Goal**: Allow users to update the description of an existing task.

**Independent Test**: Add a task, execute the `update` command, then `list` to confirm the description change.

### Implementation for User Story 3

- [ ] T016 [US3] Implement `update` command parsing and execution logic in `src/cli/main.py`. This will call `TodoService.update_task_description`.
- [ ] T017 [US3] Implement integration tests for the `update` command in `tests/integration/test_cli.py`, covering valid updates and non-existent task IDs.

## Phase 6: User Story 4 - Mark a task as complete or incomplete (Priority: P2)

**Goal**: Allow users to change the completion status of a task.

**Independent Test**: Add a task, execute `complete`/`uncomplete` commands, then `list` to confirm the status change.

### Implementation for User Story 4

- [ ] T018 [US4] Implement `complete` command parsing and execution logic in `src/cli/main.py`. This will call `TodoService.mark_task_complete`.
- [ ] T019 [US4] Implement `uncomplete` command parsing and execution logic in `src/cli/main.py`. This will call `TodoService.mark_task_incomplete`.
- [ ] T020 [US4] Implement integration tests for the `complete` and `uncomplete` commands in `tests/integration/test_cli.py`, covering valid status changes and non-existent task IDs.

## Phase 7: User Story 5 - Delete a task (Priority: P3)

**Goal**: Allow users to permanently remove a task.

**Independent Test**: Add a task, execute the `delete` command, then `list` to confirm the task is no longer present.

### Implementation for User Story 5

- [ ] T021 [US5] Implement `delete` command parsing and execution logic in `src/cli/main.py`. This will call `TodoService.delete_task`.
- [ ] T022 [US5] Implement integration tests for the `delete` command in `tests/integration/test_cli.py`, covering valid deletions and non-existent task IDs.

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T023 Refine error handling and provide user-friendly feedback for all CLI commands.
- [ ] T024 Ensure all Python code adheres to PEP8 style guidelines.
- [ ] T025 Run all unit and integration tests to ensure full functionality and stability.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
- **User Stories (Phase 3+)**: All depend on Foundational phase completion.
  - User stories can then proceed in priority order (P1 → P2 → P3).
- **Polish (Final Phase)**: Depends on all desired user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May rely on US1 and US2 for initial data setup in tests.
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May rely on US1 and US2 for initial data setup in tests.
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May rely on US1 and US2 for initial data setup in tests.

### Within Each User Story

- Tests MUST be written (T011, T013, T015, T017, T020, T022) before implementation (T010, T012, T014, T016, T018, T019, T021) in an ideal TDD cycle. However, for initial generation, they are listed together.
- Core service implementation (T010) before CLI command implementation (T012, T014, etc.).

## Parallel Opportunities

- All tasks within Phase 1 (Setup) are `[P]` parallelizable.
- The unit tests for `TodoService` (T011) can be developed in parallel with `TodoService` implementation (T010), assuming interface stability.
- Once Foundational (Phase 2) is complete, User Story 1 (Phase 3) and User Story 2 (Phase 4) can be worked on in parallel by different team members, as they are both P1 and have minimal interdependencies.
- Similarly, User Story 3 (Phase 5) and User Story 4 (Phase 6) could be parallelized.
- Within each user story, integration test creation (e.g., T013) can happen concurrently with the corresponding CLI implementation (T012), following a TDD approach.

## Implementation Strategy

### MVP First (User Story 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (`add` command)
4. Complete Phase 4: User Story 2 (`list` command)
5. **STOP and VALIDATE**: Test User Stories 1 and 2 independently. This delivers a basic, functional MVP.

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently
3. Add User Story 2 → Test independently → MVP!
4. Add User Story 3 → Test independently
5. Add User Story 4 → Test independently
6. Add User Story 5 → Test independently
7. Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together.
2. Once Foundational is done:
   - Developer A: User Story 1 and User Story 3 (P1 then P2)
   - Developer B: User Story 2 and User Story 4 (P1 then P2)
   - Developer C: User Story 5 (P3) - (can assist A or B if ahead)
3. Stories complete and integrate independently.

## Notes

- `[P]` tasks = different files, no dependencies
- `[Story]` label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
