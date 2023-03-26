class Seseorang:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

class Siswa(Seseorang):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)

class Employee(Seseorang):
    def __init__(self, name, age, address, employee_id, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.salary = salary
    def get_info(self):
        super().get_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

class Pengarang(Employee, Siswa):
    def __init__(self, name, age, address, employee_id, salary, student_id, published_books):
        Employee.__init__(self, name, age, address, employee_id, salary)
        Siswa.__init__(self, name, age, address, student_id)
        self.published_books = published_books
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
        print("Published Books:", self.published_books)