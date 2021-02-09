f = open('output05_01.txt', 'w', encoding='utf-8')

while True:
    text = input('Введите строку текста, для завершения ввода введите пустую строку->\n')
    if not text:
        f.close()
        break
    else:
        f.writelines(text + '\n')

with open('output05_01.txt', 'r', encoding='utf-8') as f:
    print('Содержимое файла->')
    print(f.read())
