print('Введите число n')
try:
    n = int(input())
    print('Сумма чисел вида n + nn + nnn, где n =', n, '->', 3*n + 2*10**len(str(n))*n + 100**len(str(n))*n)
except:
    print('Неверный ввод')