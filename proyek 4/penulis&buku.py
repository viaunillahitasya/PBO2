class penulis:
    def __init__(self, nama,buku):
        self.nama = nama
        self.buku = buku

class buku:
    def __init__(self, nama,penulis):
        self.nama = nama
        self.penulis = penulis

    def Perpustakaan(self):
        for penulis in self.penulis:
            print(penulis.nama, penulis.buku)

penulis1 = penulis("bahagia" , "tasya")
penulis2 = penulis("kasih" , "yasa")
buku = buku("3", [penulis1 , penulis2])
buku.Perpustakaan()