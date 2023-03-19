class Mahasiswa:
    def __init__(self,nama,nim):
     self.nama = nama
     self.nim = nim
    
    def info(self):
        print(f"nama:{self.nama}\nNIM: {self.nim}")

mahasiswaB = Mahasiswa("Viaunillahi tasya", "210511060")
mahasiswaB.info()           