class penjelajah:
    def __init__(self, nama, tempat):
        self.nama = nama
        self.tempat = tempat

class tempat:
    def __init__(self, nama, penjelajah):
        self.nama = nama
        self.penjelajah = penjelajah
    
    def Perpustakaan(self):
        for penjelajah in self.penjelajah:
            print(penjelajah.nama, penjelajah.tempat)

Penjelajah1 = penjelajah("viaunillahi tasya", "gunung")
Penjelajah2 = penjelajah("sabila manika", "laut")

tempat = tempat("3", [Penjelajah1, Penjelajah2])
tempat.Perpustakaan()