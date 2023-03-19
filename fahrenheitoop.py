#Nama: Viaunillahi tasya
#Nim:210511060
#kelas:reguler 2

class konversisuhu():
    def __init__(self,fahrenheit):
        self.fahrenheit = fahrenheit

    def Celcius(self):
        c = (5/9)*self.fahrenheit-32
        return c

    def reamur(self): 
        r = (4/9)*self.fahrenheit-32
        return r

    def kelvin(self):
        k = (5/9)*(self.fahrenheit-32)+278
        return k


suhu = konversisuhu(50)
Celcius = suhu.Celcius()
reamur = suhu.reamur()
kelvin =suhu .kelvin()

print(f'konfersi fahrenheit ke celcius\n\t============\t\ncelcius: {suhu.Celcius()} c')
print(f'konfersi fahrenheit ke reamur\n\t============\t\nfahrenheit: {suhu.reamur()} f')
print(f'konfersi fahrenheit ke kelvin\n\t============\t\nkelvin: {suhu.kelvin()} k')



