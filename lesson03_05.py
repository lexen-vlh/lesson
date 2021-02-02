def sum_num():
    r = 0
    while True:
        l = input('Введите строку чисел, разделенную проблелами, для выхода введите Q ->').split(" ")

        for i in l:
            try:
                r += float(i)
            except:
                if (i == 'q') or (i == 'Q'):
                    print('Сумма =', r, 'Штатное завершение работы')
                else:
                    print('Сумма =', r, 'Завершение из-за ошибочного ввода')
                return 1
        print('Сумма =', r, 'Продолжаем работать')
    return 0

sum_num()
