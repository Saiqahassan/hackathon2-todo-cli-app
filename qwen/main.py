Aimport sys
from src.services.todo_service import TodoService


def main():
    service = TodoService()
    parser = argparse.ArgumentParser(
        description="A simple in-memory Todo CLI application."
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="The description of the task")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task's description")
    update_parser.add_argument("id", type=int, help="The ID of the task to update")
    update_parser.add_argument(
        "new_description", type=str, help="The new description for the task"
    )

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="The ID of the task to mark as complete")

    # Uncomplete command
    uncomplete_parser = subparsers.add_parser("uncomplete", help="Mark a task as incomplete")
    uncomplete_parser.add_argument("id", type=int, help="The ID of the task to mark as incomplete")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="The ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        try:
            task = service.add_task(args.description)
            print(f"Task added: {task.description} (ID: {task.id})")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "list":
        tasks = service.get_all_tasks()
        if not tasks:
            print("Your todo list is empty!")
        else:
            print(f"{'ID':<4} {'Status':<10} {'Description':<40}")
            print(f"{'----':<4} {'----------':<10} {'----------------------------------------':<40}")
            for task in tasks:
                status = "[X]" if task.completed else "[ ]"
                print(f"{task.id:<4} {status:<10} {task.description:<40}")
    elif args.command == "update":
        try:
            updated_task = service.update_task_description(args.id, args.new_description)
            if updated_task:
                print(f"Task {args.id} updated.")
            else:
                print(f"Error: Task with ID {args.id} not found.", file=sys.stderr)
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == "complete":
        completed_task = service.mark_task_complete(args.id)
        if completed_task:
            print(f"Task {args.id} marked as complete.")
        else:
            print(f"Error: Task with ID {args.id} not found.", file=sys.stderr)
            sys.exit(1)
    elif args.command == "uncomplete":
        incomplete_task = service.mark_task_incomplete(args.id)
        if incomplete_task:
            print(f"Task {args.id} marked as incomplete.")
        else:
            print(f"Error: Task with ID {args.id} not found.", file=sys.stderr)
            sys.exit(1)
    elif args.command == "delete":
        deleted = service.delete_task(args.id)
        if deleted:
            print(f"Task {args.id} deleted.")
        else:
            print(f"Error: Task with ID {args.id} not found.", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
