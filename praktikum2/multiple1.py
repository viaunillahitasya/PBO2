class Warga:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip
    def belajar(self):
        print(self.nama, "sedang belajar bahasa pemrograman")

class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "bekerja sebagai", self.pekerjaan)

class WargaPekerja(Warga, Pekerja):
    def __init__(self, nama, nip, pekerjaan):
        Warga.__init__(self, nama, nip)
        Pekerja.__init__(self, nama, pekerjaan)
    def perusahaan(self):
        print(self.nama, "merupakan karyawan dengan NIP" , self.nip, "bekerja di Perusahaan manufaktur")

wrg_pekerja = WargaPekerja("tasya", "219540511860", "sistem")
wrg_pekerja.belajar() 
wrg_pekerja.bekerja() 
wrg_pekerja.perusahaan() 