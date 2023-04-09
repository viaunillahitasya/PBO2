class mahasiswa:
    def __init__(self, name):
        self.name = name
        self.anggota = anggota()

class kelompok_KKM:
    def __init__(self, name):
        self.name = name
        self.anggota =anggota()
        

class anggota:
    def __init__(self):
        self.items = []

    def add_item1(self, item):
        self.items.append(item)
        print("kelompok1:", item.name)
    def add_item2(self, item):
        self.items.append(item)
        print("kelompok2:", item.name)
            
    def remove_item(self, item):
        self.items.remove(item)
        

mahasiswa = mahasiswa("  ")
kel1 = kelompok_KKM ("viaunillahi tasya,putri,aini salsabila")
kel2 = kelompok_KKM("dewi alfi,reni susanti,dilla fadila,nanda")

print("="*40)
mahasiswa.anggota.add_item1(kel1)
mahasiswa.anggota.add_item2(kel2)
mahasiswa.anggota.items # output:[viaunillahi tasya putri aini salsabila,dewi alfi reni susanti dilla fadila nanda]

