import argparse
import json
from datetime import datetime

file_name = 'task_list.json'


def add_task(task, file_name):
    try:
        with open(file_name, 'a')as t:
            json.dump(task, t, indent=4)
            t.write("\n")
        print(f"Data saved to {file_name}")

    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Capture and save user input to a JSON file")

    parser.add_argument('task', type=str, help='Task Description')
    parser.add_argument('--status', '-s', type=str,
                        choices=['Done', 'In Progress', 'Not Done'], help="Progress of the Task")

    args = parser.parse_args()

    if args.task:
        task_data = {
            'task': args.task,
            'priority': args.status if args.status else 'medium'
        }
        add_task(task_data, file_name)
    else:
        print("Please provide a task description")


if __name__ == '__main__':
    main()
