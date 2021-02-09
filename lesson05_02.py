with open('input05_02.txt', 'r', encoding='utf-8') as f:
    print('Содержимое файла->')
    print(f.read())

with open('input05_02.txt', 'r', encoding='utf-8') as f:
    output = f.readlines()
    print('Количество строк в файле->', len(output))

    for i in range(len(output)):
        num = 1
        for j in range(len(output[i])):
            if output[i][j] == ' ':
                num += 1
        print('Количество слок в троке номер->', i + 1, 'равно->', num)
