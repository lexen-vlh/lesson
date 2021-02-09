with open('input05_03.txt', 'r', encoding='utf-8') as f:
    print('Содержимое файла->')
    print(f.read())

l_a = []
l_b = []

with open('input05_03.txt', 'r', encoding='utf-8') as f:
    l = f.read().split('\n')
    for i in l:
        i = i.split()
        if float(i[1]) < 20000:
           l_b.append(i[0])
        l_a.append(i[1])

print('У следующих сотрудинков оклад менее 20 тыс->', l_b, 'средняя величина дохода сотрудников->', sum(map(float, l_a)) / len(l_a))
