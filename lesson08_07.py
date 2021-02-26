class Complex:
    def __init__(self, real, imag):
        self.__z = complex(real, imag)

    def __add__(self, obj):
        if isinstance(obj, Complex):
            obj = obj.__z
        z = self.__z + obj
        return Complex(z.real, int(z.imag))

    def __mul__(self, obj):
        if isinstance(obj, Complex):
            obj = obj.__z
        z = self.__z * obj
        return Complex(z.real, int(z.imag))

    def __str__(self):
        return self.__z.__str__()


z1 = Complex(5, -2)
z2 = Complex(1, 4)
print(z1 + z2)
print(z1 * z2)
