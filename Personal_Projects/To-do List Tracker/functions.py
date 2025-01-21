
class task:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

def create_task(tasks):
    
    id = len(tasks) + 1
    name = input("Please enter the name of the task: ")
    description = input("Please enter the description of the task: ")

    new_task = task(id, name, description)

    return new_task

def view_tasks(tasks):

    print("[Tasks]\n")
    
    for task in tasks:
        print(f"ID: {task.id}")
        print(f"Task Name: {task.name}")
        print(f"Task Description: {task.description}\n")
