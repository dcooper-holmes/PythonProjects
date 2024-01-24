
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


#The Fish class inherits all from the 'Animal' class using 'super()'
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Swimming")

    def breath(self):
        super().breath()
        print("Doing this Underwater")

nemo = Fish()
nemo.breath()