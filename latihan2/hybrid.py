#contoh 1

# Single Inheritance
class GameObject:
  def __init__(self, x, y):
      self.x = x
      self.y = y

# Single Inheritance
class Drawable:
  def draw(self):
      print("Drawing object at: ", self.x, self.y)
# Single Inheritance
class Moveable:
  def move(self, dx, dy):
      self.x += dx
      self.y += dy
# Multiple Inheritance
class Player(GameObject, Drawable, Moveable):
  def __init__(self, x, y):
     super().__init__(x, y)
  def update(self):
     self.move(1, 1)
     self.draw()

#contoh 2     
class Seseorang:
  def __init__(self, name, age, address):
     self.name = name
     self.age = age
     self.address = address
  def get_info(self):
     print("Name:", self.name)
     print("Age:", self.age)
     print("Address:", self.address)
# Single Inheritance
class Mahasiswa(Seseorang):
  def __init__(self, name, age, address, student_id):
     super().__init__(name, age, address)
     self.student_id = student_id
  def get_info(self):
     super().get_info()
     print("Student ID:", self.student_id)
# Single Inheritance
class Employee(Seseorang):
  def __init__(self, name, age, address, employee_id, salary):
     super().__init__(name, age, address)
     self.employee_id = employee_id
     self.salary = salary
  def get_info(self):
     super().get_info()
     print("Employee ID:", self.employee_id)
     print("Salary:", self.salary)
# Multiple Inheritance
class Penulis(Employee, Mahasiswa):
  def __init__(self, name, age, address, employee_id, salary, student_id,
published_books):
      Employee.__init__(self, name, age, address, employee_id, salary)
      Mahasiswa.__init__(self, name, age, address, student_id)
      self.published_books = published_books
  def get_info(self):
     super().get_info()
     print("Student ID:", self.student_id)
     print("Published Books:", self.published_books)
     