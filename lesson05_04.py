with open('input05_04.txt', 'r', encoding='utf-8') as f:
    print('Содержимое файла->')
    print(f.read())

l = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
output = []

with open('input05_04.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        output.append(l[i[0]] + ' ' + i[1])

with open('output05_04.txt', 'w', encoding='utf-8') as f:
    f.writelines(output)

with open('output05_04.txt', 'r', encoding='utf-8') as f:
    print('Содержимое файла->')
    print(f.read())
