class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Mamalia:
    def __init__(self, jenis, habitat):
        self.jenis = jenis
        self.habitat = habitat
    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")

class Karnivora:
    def __init__(self, reproduksi, habitat):
        self.reproduksi = reproduksi
        self.habitat = habitat
    def display_info(self):
        print(f"Reproduksi: {self.reproduksi}")
        print(f"Habitat: {self.habitat}")

class Singa(Mamalia, Karnivora):
    def __init__(self, nama, umur, jenis, habitat, reproduksi):
        Hewan.__init__(self, nama, umur)
        Mamalia.__init__(self, jenis, habitat)
        Karnivora.__init__(self, reproduksi, habitat)

    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")
        print(f"Reproduksi: {self.reproduksi}")

singaA = Singa("lumba-lumba", 3, "Mamalia-Karnivora", "air", "Melahirkan")
singaA.display_info()