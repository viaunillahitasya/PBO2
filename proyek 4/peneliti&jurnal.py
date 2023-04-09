class Peneliti:
    def __init__(self, nama, jurnal):
        self.nama = nama
        self.jurnal = jurnal

class jurnal:
    def __init__(self, nama, peneliti):
        self.nama = nama
        self.peneliti = peneliti
    
    def Perpustakaan(self):
        for Peneliti in self.peneliti:
            print(Peneliti.nama, Peneliti.jurnal)

Peneliti1 = Peneliti("makhluk hidup bertahan hidup", "tasya")
Peneliti2 = Peneliti("analisis pemrograman menggunakan phyton", "Lisa")

jurnal= jurnal("3", [Peneliti1, Peneliti2])
jurnal.Perpustakaan()