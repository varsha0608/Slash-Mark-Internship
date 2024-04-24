#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import namedtuple

# Define a namedtuple to represent a task with its name and completion status
Task = namedtuple("Task", ["name", "completed"])

# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
  """
  Prints the to-do list in a formatted way.
  """
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
      status = "Done" if task.completed else "Not Done"
      print(f"{i}. {task.name} ({status})")

# Function to add a task to the to-do list
def add_task(task_name):
  """
  Adds a new task to the list with default incomplete status.
  """
  new_task = Task(task_name, False)
  tasks.append(new_task)
  print(f"Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed(task_number):
  """
  Marks a task as completed based on its position in the list.
  """
  if 1 <= task_number <= len(tasks):
    tasks[task_number - 1] = tasks[task_number - 1]._replace(completed=True)
    print(f"Task {task_number} marked as completed.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task(task_number):
  """
  Removes a task from the list based on its position.
  """
  if 1 <= task_number <= len(tasks):
    removed_task = tasks.pop(task_number - 1)
    print(f"Task '{removed_task.name}' removed from your to-do list.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Define a menu dictionary for clearer user interaction
menu_options = {
    "1": display_tasks,
    "2": add_task,
    "3": mark_completed,
    "4": remove_task,
    "5": quit,
}

# Main program loop
while True:
  print("\nOptions:")
  print("1. Display to-do list")
  print("2. Add a task")
  print("3. Mark a task as completed")
  print("4. Remove a task")
  print("5. Quit")
  choice = input("Enter your choice: ")

  if choice in menu_options:
    menu_options[choice]()
  else:
    print("Invalid choice. Please enter a valid option.")


# In[4]:


# Define a tuple to store tasks (task: string, completed: boolean)
task = ()

# Function to display the to-do list
def display_task():
  if not task:
    print("Your to-do list is empty.")
  else:
    print("To-Do List:")
    for i, task in enumerate(task, start=1):
      status = "Done" if task[1] else "Not Done"
      print(f"{i}. {task[0]} ({status})")

# Function to add a task to the to-do list
def add_task(task_name):
  new_task = (task_name, False)
  task = task + (new_task,)  # Concatenate new task tuple
  print(f"Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed(task_number):
  if 1 <= task_number <= len(task):
    updated_tasks = []
    for i, task in enumerate(task):
      if i + 1 != task_number:
        updated_task.append(task)
      else:
        updated_task.append((task[0], True))  # Update completion status
    tasks = tuple(updated_task)  # Convert list back to tuple
    print(f"Task {task_number} marked as completed.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task(task_number):
  if 1 <= task_number <= len(task):
    updated_task = []
    for i, task in enumerate(task):
      if i + 1 != task_number:
        updated_task.append(task)
    tasks = tuple(updated_tasks)  # Convert list back to tuple
    print(f"Task '{task[task_number - 1][0]}' removed from your to-do list.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
  print("\nOptions:")
  print("1. Display to-do list")
  print("2. Add a task")
  print("3. Mark a task as completed")
  print("4. Remove a task")
  print("5. Quit")
  choice = input("Enter your choice: ")

  if choice == '1':
    display_task()
  elif choice == '2':
    task_name = input("Enter the task: ")
    add_task(task_name)
  elif choice == '3':
    display_task()
    task_number = int(input("Enter the task number to mark as completed: "))
    mark_completed(task_number)
  elif choice == '4':
    display_task()
    task_number = int(input("Enter the task number to remove: "))
    remove_task(task_number)
  elif choice == '5':
    break
  else:
    print("Invalid choice. Please enter a valid option.")


# In[6]:


# Define a tuple to store tasks (task: string, completed: boolean)
tasks = ()

# Function to display the to-do list
def display_tasks():
  if not tasks:
    print("Your to-do list is empty.")
  else:
    print("To-Do List:")
    for i, tasks in enumerate(tasks, start=1):
      status = "Done" if tasks[1] else "Not Done"
      print(f"{i}. {tasks[0]} ({status})")

# Function to add a task to the to-do list
def add_task(tasks_name):
  new_task = (tasks_name, False)
  tasks = tasks + (new_tasks,)  # Concatenate new task tuple
  print(f"Tasks '{tasks_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed(tasks_number):
  if 1 <= tasks_number <= len(tasks):
    updated_tasks = []
    for i, tasks in enumerate(tasks):
      if i + 1 != tasks_number:
        updated_tasks.append(task)
      else:
        updated_tasks.append((task[0], True))  # Update completion status
    tasks = tuple(updated_tasks)  # Convert list back to tuple
    print(f"Tasks {tasks_number} marked as completed.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_tasks(tasks_number):
  if 1 <= tasks_number <= len(tasks):
    updated_tasks = []
    for i, tasks in enumerate(tasks):
      if i + 1 != tasks_number:
        updated_tasks.append(task)
    tasks = tuple(updated_tasks)  # Convert list back to tuple
    print(f"Task '{tasks[task_number - 1][0]}' removed from your to-do list.")
  else:
    print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
  print("\nOptions:")
  print("1. Display to-do list")
  print("2. Add a task")
  print("3. Mark a task as completed")
  print("4. Remove a task")
  print("5. Quit")
  choice = input("Enter your choice: ")

  if choice == '1':
    display_tasks()
  elif choice == '2':
    tasks_name = input("Enter the tasks: ")
    add_tasks(tasks_name)
  elif choice == '3':
    display_tasks()
    tasks_number = int(input("Enter the task number to mark as completed: "))
    mark_completed(tasks_number)
  elif choice == '4':
    display_tasks()
    tasks_number = int(input("Enter the task number to remove: "))
    remove_tasks(tasks_number)
  elif choice == '5':
    break
  else:
    print("Invalid choice. Please enter a valid option.")


# In[ ]:


# Define an empty list with a descriptive name
todo_list = []

# Function to display the to-do list with better formatting
def display_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, (task, completed) in enumerate(todo_list, start=1):
            status = "Done" if completed else "Not Done"
            print(f"{i}. {task}: {status}")  # Use colon for better readability

# Function to add a task with improved user feedback
def add_task(task_name):
    task = (task_name, False)
    todo_list.append(task)
    print(f"Added '{task_name}' to your to-do list.")  # Use single quotes for consistency

# Function with error handling for invalid input
def mark_completed(task_number):
    try:
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1] = (todo_list[task_number - 1][0], True)
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number. Please enter a number between 1 and", len(todo_list))
    except ValueError:
        print("Invalid input. Please enter a number.")

# Similar modification for remove_task function
def remove_task(task_number):
    try:
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Removed task '{removed_task[0]}' from your to-do list.")
        else:
            print("Invalid task number. Please enter a number between 1 and", len(todo_list))
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main program loop with consistent formatting
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '3':
        display_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_completed(task_number)
    elif choice == '4':
        display_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")


# In[ ]:




