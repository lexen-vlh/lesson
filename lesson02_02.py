print('Вводите элементы списка и нажимайте enter, для окончания ввода просто нажмите enter')
a = input('-> ')
l = []

while a != '':
    l.append(a)
    a = input('-> ')
print('Введенный список', l)

j = 0
for i in range(int(len(l)/2)):
  l[j], l[j+1] = l[j+1], l[j]
  j += 2

print('Список после обмена значениями', l)