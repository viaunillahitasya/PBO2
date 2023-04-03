class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class gajah(Animal):
    def make_sound(self):
        print("The gajah proott")

class burung(Animal):
    def make_sound(self):
        print("The burung pritt")

class Chihuahua(gajah):
    def make_sound(self):
        print("The chihuahua yaps")

class Siamese(burung):
    def make_sound(self):
        print("The Siamese purrs")

def animal_sound(animal):
    animal.make_sound()

# Instantiate objects of each class
animal = Animal()
gajah = gajah()
burung = burung()
chihuahua = Chihuahua()
siamese = Siamese()
# Call the animal_sound function for each object
animal_sound(animal) # Output: The animal makes a sound
animal_sound(gajah) # Output: The gajah proott
animal_sound(burung) # Output: The burung pritt
animal_sound(chihuahua) # Output: The chihuahua yaps
animal_sound(siamese) # Output: The Siamese purrs