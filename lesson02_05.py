l = [7, 5, 3, 3, 2]
print('Начальный набор', l)
print('Введите число (для завершения работы просто нажмите enter)')

while True:
    try:
        a = int(input('->'))
        ins = 0
        for i in range(len(l)):
            if a >= l[i]:
                if a == l[i]:
                    l.insert(i+1, a)
                else:
                    l.insert(i, a)
                ins += 1
                break
        if ins == 0:
            l.append(a)
        print('Текущий набор', l)
    except:
        print('Завершение работы')
        break
