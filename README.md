# Task Manager CLI

A simple command line task management application built with Python. The project demonstrates object-oriented programming, file handling, JSON based data persistence, exception handling, and a clean modular structure.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Automatically save tasks to a JSON file
* Load existing tasks on startup
* Lightweight with no external dependencies

## Project Structure

```text
task_manager/
├── app.py
├── task_manager.py
└── tasks.json
```

## Requirements

* Python 3.8 or later

## Installation

Clone the repository:

```bash
git clone https://github.com/agentuser5232/task-manager.git
```

Navigate to the project directory:

```bash
cd task-manager
```

## Usage

Run the application:

```bash
python app.py
```

### Menu

```text
Task Manager

1. View Tasks
2. Add Task
3. Complete Task
4. Exit
```

## Example

```text
Select an option: 2
Task title: Finish project documentation
Task added.

Select an option: 1

1. Finish project documentation [Pending]

Select an option: 3
Task number: 1
Task marked as completed.
```

## Technologies Used

* Python 3
* JSON
* Standard Library (`json`, `os`)

## Learning Objectives

This project demonstrates:

* Object-oriented programming
* Modular code organization
* File handling
* JSON serialization
* Exception handling
* Command line application development

## Future Improvements

* Delete tasks
* Edit task titles
* Task priorities
* Due dates
* Search and filter tasks
* Colored terminal output
