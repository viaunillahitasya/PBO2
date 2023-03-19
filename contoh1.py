class motor:
    def __init__(self, merk, warna): 
     self.merk=merk
     self.warna=warna
    def info(self):
        print(f"motor{self.merk} berwarna {self.warna}")

motorA=motor("yamaha","hijau")
motorA.info()#output:motor yamaha berwarna hijau  
