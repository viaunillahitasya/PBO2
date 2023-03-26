#Nama: Viaunillahi tasya
#Nim:210511060
#kelas:reguler 2

class konversisuhu():
    def __init__(self,kelvin):
        self.kelvin = kelvin

    def Celcius(self):
        c = self.kelvin-273
        return c

    def fahrenheit(self): 
        f = ((self.kelvin-273)*(9/5))+32
        return f

    def reamur(self):
        R = (4/5)*(self.kelvin-273)
        return R


suhu = konversisuhu(50)
Celcius = suhu.Celcius()
fahrenheit = suhu.fahrenheit()
reamur =suhu.reamur()

print(f'konfersi kelvin ke celcius\n\t============\t\ncelcius: {suhu.Celcius()} c')
print(f'konfersi kelvin ke fahrenheit\n\t===========\t\nfahrenheit: {suhu.fahrenheit()} f')
print(f'konfersi kelvin ke reamur\n\t===========\t\nkelvin: {suhu.reamur()} R')



