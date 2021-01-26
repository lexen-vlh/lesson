print('Введите время в секундах')
try:
    a = int(input())
    print('Вы ввели', a, 'секунд')

    h = a // 3600
    m = (a - h * 3600) // 60
    s = a - h * 3600 - m * 60

    out = 'В формате чч:мм:сс это - '

    if h < 10:
        out = out + '0' + str(h) + ":"
    else:
        out = out + str(h) + ":"

    if m < 10:
        out = out + '0' + str(m) + ":"
    else:
        out = out + str(m) + ":"

    if s < 10:
        out = out + '0' + str(s)
    else:
        out = out + str(s)

    print(out)
except:
    print('Неверный ввод')