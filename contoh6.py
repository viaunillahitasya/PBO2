class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def subtract(x, y):    
        return x - y
    @staticmethod
    def multiply(x, y):   
        return x * y
    @staticmethod
    def divide(x, y):    
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(3, 5))       #output:7
print(Kalkulator.subtract(6, 8))    #output:4

# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(5, 7))  # Output: 24
print(Kalkulator.divide(17, 6))  # Output: 3.0