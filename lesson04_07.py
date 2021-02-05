from itertools import count
from math import factorial

def fact(n):
    for i in count(1):
        if i <= n:
            yield factorial(i)
        else:
            break

l = []

try:
    for el in fact(int(input('Введите n->'))):
        l.append(el)
    print('Список факториалов:', l)

except:
    print('Неверный ввод')


