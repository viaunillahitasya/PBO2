#contoh 1
class Animal:
  def __init__(self, name):
     self.name = name
  def speak(self):
     print("The animal speaks")

class Dog(Animal):
  def __init__(self, name, breed):
     super().__init__(name)
     self.breed = breed
  def speak(self):
     print("The dog barks")

class Bulldog(Dog):
  def __init__(self, name, breed, origin):
     super().__init__(name, breed)
     self.origin = origin
  def speak(self):
     print("The bulldog growls")

#contoh 2
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
   def __init__(self, name, age, id, salary):
       super().__init__(name, age)
       self.id = id
       self.salary = salary
   def get_details(self):
       super().get_details()
       print(f"ID: {self.id}, Salary: {self.salary}")

class Manager(Employee):
   def __init__(self, name, age, id, salary, department):
       super().__init__(name, age, id, salary)
       self.department = department
   def get_details(self):
       super().get_details()
       print(f"Department: {self.department}")

#contoh 3
class Animal:
  def __init__(self, name):
     self.name = name
  def speak(self):
     print(f"{self.name} speaks")

class Bird(Animal):
  def __init__(self, name, wingspan):
      super().__init__(name)
      self.wingspan = wingspan
  def fly(self):
      print(f"{self.name} is flying with a wingspan of {self.wingspan}")

class Parrot(Bird):
  def __init__(self, name, wingspan, color):
      super().__init__(name, wingspan)
      self.color = color
  def speak(self):
      print(f"{self.name} is a {self.color} parrot that talks")

parrot = Parrot("Rio", 12, "blue")
parrot.speak() # Output: Rio is a blue parrot that talks
parrot.fly() # Output: Rio is flying with a wingspan of 12 


