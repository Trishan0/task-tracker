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
    
    # Create new task
    new_task = {
        'task': task_description,
        'status': status if status else 'Not Done',
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Add new task to the list
    task_list["tasks"].append(new_task)
    
    # Save updated task list
    save_tasks(task_list, file_name)

def main():
    parser = argparse.ArgumentParser(
        description="Capture and save tasks to a JSON file")

    parser.add_argument('task', type=str, help='Task Description')
    parser.add_argument('--status', '-s', type=str,
                        choices=['Done', 'In Progress', 'Not Done'], 
                        default='Not Done',
                        help="Progress of the Task")

    args = parser.parse_args()

    if args.task:
        add_task(args.task, args.status, FILE_NAME)
    else:
        print("Please provide a task description")

if __name__ == '__main__':
    main()