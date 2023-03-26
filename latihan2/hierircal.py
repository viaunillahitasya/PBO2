#contoh 1

class Animal:
   def __init__(self, name, color):
     self.name = name
     self.color = color
   def get_name(self):
     return self.name
   def get_color(self):
     return self.color

class Mammal(Animal):
   def __init__(self, name, color, fur):
     super().__init__(name, color)
     self.fur = fur
   def get_fur(self):
     return self.fur

class Bird(Animal):
   def __init__(self, name, color, wingspan):
     super().__init__(name, color)
     self.wingspan = wingspan
   def get_wingspan(self):
     return self.wingspan

# Hierarchical Inheritance
class Reptile(Mammal):
   def __init__(self, name, color, fur, scale):
     super().__init__(name, color, fur)
     self.scale = scale
   def get_scale(self):
     return self.scale

#contoh 2

class Employee:
   def __init__(self, name, age, salary):
     self.name = name
     self.age = age
     self.salary = salary
   def get_name(self):
     return self.name
   def get_age(self):
     return self.age
   def get_salary(self):
     return self.salary

class Manager(Employee):
   def __init__(self, name, age, salary, department):
     super().__init__(name, age, salary)
     self.department = department
   def get_department(self):
     return self.department

class Programmer(Employee):
   def __init__(self, name, age, salary, language):
     super().__init__(name, age, salary)
     self.language = language
   def get_language(self):
     return self.language

# Hierarchical Inheritance
class SeniorProgrammer(Programmer):
   def __init__(self, name, age, salary, language, level):
     super().__init__(name, age, salary, language)
     self.level = level
   def get_level(self):
     return self.level   

#contoh 3
class Kendaraan:
   def __init__(self, nama):
     self.nama = nama
   def get_nama(self):
     return self.nama
class Mobil(Kendaraan):
   def __init__(self, nama, merek):
     super().__init__(nama)
     self.merek = merek
   def get_merek(self):
     return self.merek

class SepedaMotor(Kendaraan):
   def __init__(self, nama, tipe):
     super().__init__(nama)
     self.tipe = tipe
   def get_tipe(self):
     return self.tipe

# turunan Hierarchical Inheritance
class Truk(Mobil):
   def __init__(self, nama, merek, kapasitas):
     super().__init__(nama, merek)
     self.kapasitas = kapasitas
   def get_kapasitas(self):
     return self.kapasitas
# turunan Hierarchical Inheritance
class MotorListrik(SepedaMotor):
   def __init__(self, nama, tipe, daya):
     super().__init__(nama, tipe)
     self.daya = daya
   def get_daya(self):
     return self.daya       

#contoh 4
class Shape:
   def __init__(self, name, color):
     self.name = name
     self.color = color
   def get_name(self):
     return self.name
   def get_color(self):
     return self.color

class TwoDimensional(Shape):
   def __init__(self, name, color, sides):
     super().__init__(name, color)
     self.sides = sides
   def get_sides(self):
     return self.sides

class ThreeDimensional(Shape):
   def __init__(self, name, color, faces):
     super().__init__(name, color)
     self.faces = faces
   def get_faces(self):
     return self.faces

# Hierarchical Inheritance
class Sphere(ThreeDimensional):
   def __init__(self, name, color, faces, radius):
     super().__init__(name, color, faces)
     self.radius = radius
   def get_radius(self):
     return self.radius

#contoh 5
class AkunBank:
   def __init__(self, nomor_akun, saldo):
     self.nomor_akun = nomor_akun
     self.saldo = saldo
   def get_nomor_akun(self):
     return self.nomor_akun
   def get_saldo(self):
     return self.saldo

class AkunTabungan(AkunBank):
   def __init__(self, nomor_akun, saldo, persentase_bunga):
     super().__init__(nomor_akun, saldo)
     self.persentase_bunga = persentase_bunga
   def get_persentase_bunga(self):
     return self.persentase_bunga

class CekAkun(AkunBank):
   def __init__(self, nomor_akun, saldo, overdraft_limit):
     super().__init__(nomor_akun, saldo)
     self.overdraft_limit = overdraft_limit
   def get_overdraft_limit(self):
     return self.overdraft_limit

# Hierarchical Inheritance
class JointAccount(AkunTabungan):
   def __init__(self, nomor_akun, saldo, persentase_bunga, owners):
     super().__init__(nomor_akun, saldo, persentase_bunga)
     self.owners = owners
   def get_owners(self):
     return self.owners    