
class task:

    def __init__(self, id, name, description, completed):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

def create_task(tasks):
    
    id = len(tasks) + 1
    name = input("Please enter the name of the task: ")
    description = input("Please enter the description of the task: ")
    completed = False

    new_task = task(id, name, description, completed)

    return new_task

def view_tasks(tasks):

    print("[Tasks]\n")
    
    for task in tasks:
        print(f"ID: {task.id}")
        print(f"Task Name: {task.name}")
        print(f"Task Description: {task.description}")
        print(f"Task Completed: {task.completed}\n")

def delete_task(tasks):

    while True:
        for task in tasks:
            print(f"Task ID: {task.id}")
            print(f"Task Name: {task.name}\n")

        selection = int(input("Enter the ID of the task you would like to delete: ")) - 1

        tasks.pop(selection)

        if len(tasks) == 0:
           break
        else:
            if input("Would you like to delete another task? Y/N: ").lower() == "y":
                continue
            else:
                break