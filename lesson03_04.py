def exponentiation1(arg1, arg2):
    return 1 / arg1 ** abs(arg2)

def exponentiation2(arg1, arg2):
    i = 0
    r = arg1
    while i < abs(arg2) - 1:
        r *= arg1
        i += 1
    return 1 / r

print('Использование **', exponentiation1(5, -3))
print('Использование цикла', exponentiation2(5, -3))
