from functools import reduce

l = [i for i in range(100, 1000+1) if i%2 == 0]

print('Итоговый список->', l)

def multiplication(a, b):
    return a * b

print('Результат умножения->', reduce(multiplication, l))
