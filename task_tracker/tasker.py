import argparse
from task_tracker.model import add_task, update_task, delete_task, list_tasks, FILE_NAME

def main():
    parser = argparse.ArgumentParser(
        description="Capture and save tasks to a JSON file")

    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    #Add task command
    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument('task', type=str, help="Task Description")
    add_parser.add_argument('--status', '-s', choices=['not done','in progress','done'], default='not done', help="Progress of the task")
    

    #Update task command
    update_parser = subparsers.add_parser('update', help="Update an existing task")
    update_parser.add_argument('id',type=int, help="Task ID")
    update_parser.add_argument('--description','-d',type=str, help="New task description")
    update_parser.add_argument('--status','-s', type=str,
                               choices=['not done', 'in progress', 'done'],
                               default='not done',
                               help="New task status")
    
    # Delete task command
    delete_parser = subparsers.add_parser('delete', help="Delete a task")
    delete_parser.add_argument('id', type=int, help="Task ID")
    
    # View task command
    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.add_argument("status", type=str, nargs='?', default=None, help="Status of the tasks to list (optional)")

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.task, args.status, FILE_NAME)
    elif args.command == 'update':
        if not (args.description or args.status):
            print("Please provide either new description or status to update")
            return
        update_task(args.id, args.description, args.status)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        parser.print_help()
