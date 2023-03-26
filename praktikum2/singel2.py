class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bermain(self):
        print(self.nama, "sedang bermain bola")
class harimau(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def berjenis(self):
       print(self.nama, "merupakan harimau berjenis", self.jenis_bulu, "berumur", self.umur, "tahun")
harimauA = harimau("Boly", 3, "Benggala")
harimauA.bermain()
harimauA.berjenis() 