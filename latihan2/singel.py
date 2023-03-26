#contoh 1
class Hewan:
   def __init__(self, nama, umur):
     self.nama = nama
     self.umur = umur
   def bergerak(self):
     print(self.nama, "bergerak")

class Kucing(Hewan):
   def __init__(self, nama, umur, jenis_bulu):
     super().__init__(nama, umur)
     self.jenis_bulu = jenis_bulu
   def bersuara(self):
     print("Meow!")

kucingA = Kucing("Kitty", 2, "Persia")
kucingA.bergerak() # output: Kitty bergerak
kucingA.bersuara() # output: Meow!

#contoh 2
class Manusia:
  def __init__(self, nama, umur):
      self.nama = nama
      self.umur = umur
  def berbicara(self):
      print(f"{self.nama} sedang berbicara.")

class Dosen(Manusia):
   def __init__(self, nama, umur, nip):
     super().__init__(nama, umur)
     self.nip = nip

   def mengajar(self):
          print(f"{self.nama} dengan NIP {self.nip} sedang mengajar.")

dosenA = Dosen("Budi", 35, "123456")
dosenA.berbicara() # Output: Budi sedang berbicara.
dosenA.mengajar() # Output: Budi dengan NIP 123456 sedang mengajar.

#contoh 3
class Kendaraan:
   def __init__(self, jenis, merk, warna):
     self.jenis = jenis
     self.merk = merk
     self.warna = warna
   def berkendara(self):
     print("Kendaraan ini sedang berjalan.")
     
class SepedaMotor(Kendaraan):
   def __init__(self, jenis, merk, warna, cc):
     super().__init__(jenis, merk, warna)
     self.cc = cc
   def belok(self):
     print("Sepeda motor ini sedang belok.")

motorA = SepedaMotor("Sepeda Motor", "Honda", "Merah", 150)
motorA.berkendara() # Output: Kendaraan ini sedang berjalan.
motorA.belok() # Output: Sepeda motor ini sedang belok.