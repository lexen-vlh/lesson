print('Введите целое положительное число')
try:
    a = int(input())
    if a > 0:
        b = 0
        while a > 0:
            c = a
            a //= 10
            if b < (c - a*10):
                b = c - a*10
        print('Самое большое число', b)
    else:
        print('Неверный ввод, число меньше нуля')
except:
    print('Неверный ввод')