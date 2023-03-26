#Nama:viaunillahi tasya
#kelas:Reguler 2
#Nim:210511060


class TemperatureConverter:
   def __init__(self, celsius):
       self.celsius = celsius

   def to_reamur(self):
       return (4/5) * self.celsius

   def to_kelvin(self):
        return self.celsius + 273.15

   def to_fahrenheit(self):
       return (9/5) * self.celsius + 32

temperature = TemperatureConverter(59)
fahrenheit = temperature.to_fahrenheit()
kelvin = temperature.to_kelvin()
reamur = temperature.to_reamur()

print(f"{temperature.celsius} Derajat Celcius = {reamur} Derajat Reamur")
print(f"{temperature.celsius} Derajat Celcius = {kelvin} Kelvin")
print(f"{temperature.celsius} Derajat Celcius = {fahrenheit} Derajat Fahrenheit")