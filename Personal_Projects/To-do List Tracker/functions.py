

class task:

    def __init__(self, name, description):
        self.name = name
        self.description = description

def create_task():
        
    name = input("Please enter the name of the task: ")
    description = input("Please enter the description of the task: ")

    new_task = task(name, description)

    return new_task    
