class membentuk:
   def area(self):
     pass

class persegi(membentuk):
   def __init__(self, lebar, tinggi):
     self.lebar = lebar
     self.tinggi = tinggi
   def area(self):
     return self.lebar * self.tinggi

class lingkaran(membentuk):
   def __init__(self, radius):
     self.radius = radius
   def area(self):
     return 3.14 * self.radius ** 2

membentuk = [persegi(6, 5), lingkaran(9)]
for membentuk in membentuk:
    print(membentuk.area())