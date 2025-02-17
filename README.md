# task-tracker
<div align="center">
    <img src="https://socialify.git.ci/Trishan0/task-tracker/image?forks=1&issues=1&language=1&name=1&pulls=1&stargazers=1&theme=Auto" alt="Task Tracker CLI" width="640" height="320" />
</div>
<br><br>
<br>

<div align='center' style=" display: grid;">

  [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sanjanatrishan@gmail.com)
  [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Trishan0)
  [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@trishan-fernando)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/trishan-fernando/)
</div>

---

# Task Tracker CLI Project

The **Task Tracker** is a command-line interface (CLI) project designed to help you track and manage tasks. It allows you to add, update, and delete tasks, as well as mark tasks as "in-progress" or "done." This project will help you practice essential programming skills, including working with the filesystem, handling user inputs, and building a basic CLI application.

## Requirements

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

- Add, Update, and Delete tasks
- Mark a task as "in progress" or "done"
- List all tasks
- List all tasks that are marked as "done"
- List all tasks that are marked as "not done"
- List all tasks that are marked as "in progress"

### Constraints

- You can use any programming language to build this project.
- Use **positional arguments** in the command line to accept user inputs.
- Use a **JSON file** to store the tasks in the current directory.
- The JSON file should be created if it does not exist.
- Use the **native filesystem module** of your programming language to interact with the JSON file.
- Do not use any external libraries or frameworks to build this project.
- Ensure to handle errors and edge cases gracefully.

## Example Commands

Here are some example commands and their usage:

```bash
# Adding a new task
tasker add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
tasker update 1 "Buy groceries and cook dinner"
tasker delete 1

# Marking a task as in progress or done
tasker mark-in-progress 1
tasker mark-done 1

# Listing all tasks
tasker list

# Listing tasks by status
tasker list done
tasker list "not done"
tasker list "in-progress"
```

## Task Properties

Each task should have the following properties:

- `id`: A unique identifier for the task
- `description`: A short description of the task
- `status`: The status of the task (`todo`, `in-progress`, `done`)
- `createdAt`: The date and time when the task was created
- `updatedAt`: The date and time when the task was last updated

When adding a new task, these properties should be stored in the JSON file and updated when modifying it.

## Conclusion

This project offers an opportunity to improve your programming and CLI development skills. You can practice interacting with the filesystem, handling JSON data, and managing user input via the command line while building a useful task-tracking tool.

Original Project Link: [Task Tracker CLI](https://roadmap.sh/projects/task-tracker)

---

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Trishan0/task-tracker.git
    cd task-tracker
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

### Usage

1. Run the Task Tracker CLI:
    ```sh
    pip install -e .
    task-tracker    
    ```

2. Follow the on-screen instructions to add, view, update, or delete tasks.

### Basic Commands

- **Add a Task**: 
    ```sh
    tasker add "Task Description"
    ```

- **View All Tasks**: 
    ```sh
    tasker list [status]
    ```

- **Update a Task**: 
    ```sh
    tasker update <task_id> "New Task Description"
    ```

- **Delete a Task**: 
    ```sh
    tasker delete <task_id>
    ```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
