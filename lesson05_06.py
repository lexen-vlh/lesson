with open('input05_06.txt', 'r', encoding='utf-8') as f:
    print('Содержимое файла->')
    print(f.read())

output = {}
with open('input05_06.txt', 'r', encoding='utf-8') as f:
    for i in f:
        l = i.split()
        output[l[0][:l[0].find(':')]] = 0
        for j in range(1, 4):
            if (l[j][:l[j].find('(')]) != '':
                output[l[0][:l[0].find(':')]] += int(l[j][:l[j].find('(')])

print('Общее количество занятий->', output)
