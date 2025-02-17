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
    else:
        parser.print_help()

if __name__ == '__main__':
    main()