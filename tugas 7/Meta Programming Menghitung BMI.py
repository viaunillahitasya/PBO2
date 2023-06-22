print('viaunillahi tasya\n210511060\nT121B(R2)\n')

class MenghitungBMIMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def pria(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 10/100
        cls.pria = classmethod(pria)

        def wanita(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 15/100
        cls.wanita = classmethod(wanita)
class Ideal(metaclass=MenghitungBMIMeta):
    pass
A = Ideal()
B = A.pria(180)
C = A.wanita(160)
print('BMI Pria:',B)
print('BMI Wanita:',C)