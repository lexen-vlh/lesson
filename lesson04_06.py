from itertools import count
from itertools import cycle

def gen_int(a, b):
    l = []
    for i in count(a):
        if i <= b:
            l.append(i)
        else:
            return l

def gen_cyc(l, num):
    l_c = []
    i = 0
    n = cycle(l)
    while i < num:
        l_c.append(next(n))
        i += 1
    return l_c

print('Генератор целых чисел:')
print('Результат:', gen_int(int(input('начиная с->')), int(input('заканчивая->'))))

print('Генератор повторяющихся элементов:')
print('Результат:', gen_cyc([1, 2, 3], int(input('повторений->'))))
