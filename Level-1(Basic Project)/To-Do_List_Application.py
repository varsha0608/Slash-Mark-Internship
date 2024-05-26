Feature:
*Stay Organized: Keep track of your tasks in one convenient place.
*Boost Productivity: Prioritize tasks and focus on what matters most.
*Never Miss a Deadline: Set reminders and deadlines for important tasks.
*Achieve Your Goals: Break down large projects into smaller, manageable tasks.


How to Use:
The program presents a menu with options to manage your to-do list. Simply enter the corresponding number to perform the desired action:
*Display to-do list: View all tasks, including their completion status.
*Add a task: Enter the name of the new task to add it to the list.
*Mark a task as completed: Select a task by its number to mark it as done.
*Remove a task: Choose a task by its number to delete it from the list.
*Quit: Exit the program.
    
                                                       

  

todo_list = []

def display_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, (task, completed) in enumerate(todo_list, start=1):
            status = "Done" if completed else "Not Done"
            print(f"{i}. {task}: {status}")  # Use colon for better readability

def add_task(task_name):
    task = (task_name, False)
    todo_list.append(task)
    print(f"Added '{task_name}' to your to-do list.")  # Use single quotes for consistency
def mark_completed(task_number):
    try:
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1] = (todo_list[task_number - 1][0], True)
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number. Please enter a number between 1 and", len(todo_list))
    except ValueError:
        print("Invalid input. Please enter a number.")
def remove_task(task_number):
    try:
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Removed task '{removed_task[0]}' from your to-do list.")
        else:
            print("Invalid task number. Please enter a number between 1 and", len(todo_list))
    except ValueError:
        print("Invalid input. Please enter a number.")
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
