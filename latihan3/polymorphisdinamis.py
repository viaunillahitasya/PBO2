class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")

class Chihuahua(Dog):
    def make_sound(self):
        print("The chihuahua yaps")

class Siamese(Cat):
    def make_sound(self):
        print("The Siamese purrs")

def animal_sound(animal):
    animal.make_sound()

# Instantiate objects of each class
animal = Animal()
dog = Dog()
cat = Cat()
chihuahua = Chihuahua()
siamese = Siamese()
# Call the animal_sound function for each object
animal_sound(animal) # Output: The animal makes a sound
animal_sound(dog) # Output: The dog barks
animal_sound(cat) # Output: The cat meows
animal_sound(chihuahua) # Output: The chihuahua yaps
animal_sound(siamese) # Output: The Siamese purrs