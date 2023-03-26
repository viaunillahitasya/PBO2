#Nama: Viaunillahi tasya
#Nim:210511060
#kelas:reguler 2

class konversisuhu():
    def __init__(self,reamur):
        self.reamur = reamur

    def Celcius(self):
        c = self.reamur*(5/4)
        return c

    def fahrenheit(self): 
        f = (9/4)*self.reamur+32
        return f

    def kelvin(self):
        k = (5/4)*(self.reamur+273)
        return k


suhu = konversisuhu(50)
Celcius = suhu.Celcius()
fahrenheit = suhu.fahrenheit()
kelvin =suhu .kelvin()

print(f'konfersi reamur ke celcius\n\t============\t\ncelcius: {suhu.Celcius()} c')
print(f'konfersi reamur ke fahrenheit\n\t============\t\nfahrenheit: {suhu.fahrenheit()} f')
print(f'konfersi reamur ke kelvin\n\t============\t\nkelvin: {suhu.kelvin()} k')



