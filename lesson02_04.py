print('Введите строку')
s = input('->')
w = []

try:
    for i in range(s.count(' ') + 1):
        w = s.split()
        if len(str(w)) <= 10:
            print(i+1, w[i])
        else:
            print(i+1, w[i][0:10])
except:
    print('Лишние пробелы в строке')
