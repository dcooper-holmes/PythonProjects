
class task:

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

def create_task():
        
    name = input("Please enter the name of the task: ")
    description = input("Please enter the description of the task: ")

    new_task = task(name, description)

    return new_task

def view_tasks(tasks):

    print("[Tasks]\n")
    
    for task in tasks:
        print(f"Task Name: {task.name}")
        print(f"Task Description: {task.description}\n")
