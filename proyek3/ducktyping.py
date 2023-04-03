class Kambing:
    def bersuara(self):
        print("Mbeeh")

class gajah:
    def bersuara(self):
        print("proott")

def cetak_suara(objek):
    objek.bersuara()

Kambing = Kambing()
gajah = gajah()
cetak_suara(Kambing) # Output: Mbeeh
cetak_suara(gajah) # Output: proott