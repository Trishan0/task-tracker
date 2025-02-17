import argparse
import json
from datetime import datetime
import os

FILE_NAME = 'task_list.json'

def load_tasks(file_name):
    """Load existing tasks from the JSON file."""
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"tasks": []}
    return {"tasks": []}

def save_tasks(tasks, file_name):
    """Save all tasks to the JSON file."""
    try:
        with open(file_name, 'w') as f:
            json.dump(tasks, f, indent=4)
        print(f"Data successfully saved to {file_name}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def add_task(task_description, status, file_name):
    """Add a new task to the task list."""
    # Load existing tasks
    task_list = load_tasks(file_name)
    
    #Determine the next task ID
    if task_list["tasks"]:
        next_id = max(task["id"] for task in task_list["tasks"]) + 1
    else:
        next_id = 1
    
    # Create new task
    new_task = {
        'id': next_id,
        'task': task_description,
        'status': status if status else 'Not Done',
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }
    
    # Add new task to the list
    task_list["tasks"].append(new_task)
    
    # Save updated task list
    save_tasks(task_list, file_name)
    print(f"Task added with ID: {new_task['id']}")
    return new_task['id']

def update_task(task_id, new_description=None, new_status=None, file_name=FILE_NAME):
    """Update an existing task by ID."""
    task_list = load_tasks(file_name)
    
    for task in task_list["tasks"]:
        if task["id"] == task_id:
            if new_description:
                task["task"] = new_description
            if new_status:
                task["status"] = new_status
            task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(task_list, file_name)
            print(f"Task {task_id} updated successfully")
            return True
        
    print(f"Task with ID {task_id} not found")
    return False       
     
def delete_task(task_id, file_name=FILE_NAME):
    """"Delete a task by ID"""
    
    task_list = load_tasks(file_name)
    
    initial_length = len(task_list["tasks"])
    task_list["tasks"] = [task for task in task_list["tasks"] if task["id"] != task_id]
    
    if len(task_list["tasks"]) < initial_length:
        save_tasks(task_list, file_name)
        print(f"Task {task_id} deleted successfully")
        return True
    else:
        print(f"Task with ID {task_id} not found")
        return False
    
def list_tasks(status=None, file_name=FILE_NAME):
    """
    List tasks, optionally filtered by status.
    
    Args:
        status (str, optional): Filter tasks by this status. If None, shows all tasks
        file_name (str): The JSON file storing the tasks
    """
    task_list = load_tasks(file_name)
    
    if not task_list["tasks"]:
        print("No tasks found")
        return
    
    # Filter tasks if status is provided
    filtered_tasks = task_list["tasks"]
    if status:
        status = status.title()
        filtered_tasks = [task for task in task_list["tasks"] 
                         if task["status"].lower() == status.lower()]
        
        if not filtered_tasks:
            print(f"No tasks found with status: {status}")
            return
    
    if status:
        print(f"\nShowing tasks with status: {status}")
    else:
        print("\nShowing all tasks:")
    
    print("-" * 50)
    
    # Display tasks with consistent formatting
    for task in filtered_tasks:
        print(f"ID: {task['id']}")
        print(f"Task: {task['task']}")
        print(f"Status: {task['status']}")
        print(f"Created: {task['created_at']}")
        print(f"Last Updated: {task['updated_at']}")
        print("-" * 50)
    
    # Show summary count
    print(f"\nTotal tasks shown: {len(filtered_tasks)}")


def main():
    parser = argparse.ArgumentParser(
        description="Capture and save tasks to a JSON file")

    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    #Add task command
    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument('task', type=str, help="Task Description")
    add_parser.add_argument('--status', '-s', choices=['todo','in-progress','done'], default='not done', help="Progress of the task")
    

    #Update task command
    update_parser = subparsers.add_parser('update', help="Update an existing task")
    update_parser.add_argument('id',type=int, help="Task ID")
    update_parser.add_argument('--description','-d',type=str, help="New task description")
    update_parser.add_argument('--status','-s', type=str,
                               choices=['done', 'in progress', 'not done'],
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

if __name__ == '__main__':
    main()