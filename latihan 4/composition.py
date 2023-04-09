class peneliti:
   def __init__(self, nama, umur):
     self.nama = nama
     self.umur = umur

class jurnal:
   def __init__(self, nama, peneliti):
     self.nama = nama
     self.peneliti = peneliti
   def daftar_peneliti(self):
    for peneliti in self.peneliti:
        print(peneliti.nama, peneliti.umur)
        
peneliti1 = peneliti("Andi", 25)
peneliti2 = peneliti("Budi", 30)
jurnal = jurnal("ABC", [peneliti1, peneliti2])
jurnal.daftar_peneliti()