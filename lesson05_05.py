from random import randint

try:
    m = int(input('Введите целое положительное число - верхнюю границу->'))
    x = [randint(0, m) for p in range(0, int(input('Введите целое положительное число - количество чисел->')))]

    with open('output05_05.txt', 'w+', encoding='utf-8') as f:
        for i in x:
            f.write(str(i) + ' ')

    with open('output05_05.txt', 'r', encoding='utf-8') as f:
        print('Содержимое файла->')
        print(f.read())

    y = []

    with open('output05_05.txt', 'r', encoding='utf-8') as f:
        l = f.read().split(' ')
        for i in l:
            if not i:
                break
            else:
                y.append(i)

    print('Сумма чисел в файле->', sum(map(int, y)))
except:
    print('Неверный ввод')
