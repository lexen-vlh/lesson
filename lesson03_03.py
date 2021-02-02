def sum2(a, b, c):
    if (a >= c) and (b >= c):
        return a + b
    elif (a > b) and (a < c):
        return a + c
    else:
        return b + c

try:
    print('Введите три целых числа')
    a=int(input('a->'))
    b=int(input('b->'))
    c=int(input('c->'))
    print('Сумма двух наибольших чисел равна', sum2(a, b, c))
except:
    print('Невернный ввод')