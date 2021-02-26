class MyZeroDivisionError(Exception):
    error = 'Ошибка деления на ноль'

    def __str__(self):
        return self.error


class Number(float):
    def __truediv__(self, number):
        if number is not None and not number:
            raise MyZeroDivisionError

        return Number(float(self) / float(number))


num1 = Number(123.45)
num2 = Number(67.8)
num3 = Number(0)

try:
    print(num1/num2)
    print(num2/num3)
except MyZeroDivisionError as e:
    print(e)
