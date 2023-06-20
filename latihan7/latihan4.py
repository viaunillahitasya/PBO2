class CelciusMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.suhu_standar = ""
    
    def to_fahrenheit(cls, suhu):
        return (suhu * 9/5) + 32
    
    def to_reamur(cls, suhu):
        return suhu * 4/5

    def to_kelvin(cls, suhu):
        return suhu + 273.15

class Celcius(metaclass=CelciusMeta):
    def __init__(self, suhu):
        self.suhu = suhu
    
    def ke_unit(self, unit):
        if unit == "Fahrenheit":
            self.suhu = self.__class__.to_fahrenheit(self.suhu)
            self.__class__.suhu_standar = "Fahrenheit"
        elif unit == "Reamur":
            self.suhu = self.__class__.to_reamur(self.suhu)
            self.__class__.suhu_standar = "Reamur"
        elif unit == "Kelvin":
            self.suhu = self.__class__.to_kelvin(self.suhu)
            self.__class__.suhu_standar = "Kelvin"
        elif unit == "Celcius":
            pass # do nothing
        else:
            raise ValueError(f"Unit {unit} tidak dikenal.")
    def __repr__(self):
        return f"{self.suhu:.2f} {self.__class__.suhu_standar}"
# Membuat objek suhu dengan nilai 100 Celcius
c = Celcius(100)
# Mengubah objek suhu menjadi Fahrenheit
c.ke_unit("Fahrenheit")
print(c)
