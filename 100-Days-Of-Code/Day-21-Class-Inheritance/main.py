
class Animal:
    def __init__(self):
        num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


#The Fish class inherits all from the 'Animal' class using 'super()'
class Fish(Animal):
    def __init__(self):
        super().__init__()