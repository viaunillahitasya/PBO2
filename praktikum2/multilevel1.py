class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("The animal speaks")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print("The cat groaned")

class Persia(Cat):
    def __init__(self, name, breed, origin):
        super().__init__(name, breed)
        self.origin = origin
    def speak(self):
        print("The Persia", self.name , "is breed and origin in", self.origin)
persia = Persia("moly", "Persia", "Central Asia")
persia.speak()