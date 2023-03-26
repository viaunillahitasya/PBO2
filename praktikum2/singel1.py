class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berjalan(self):
        print(f"{self.jenis} sedang berjalan lurus.")

class Motor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
        print(f"{self.jenis} berwarna {self.warna} dengan merk {self.merk} tiba tiba berbelok.")

mobilA = Motor("Motor", "honda", "Merah", 250)
mobilA.berjalan() 
mobilA.belok()
