gs = []
a = {}
num = int(input("Укажите количество товаров ->"))
cur = 1

while cur <= num:
    fs = {}
    print('Товар номер', cur)
    while input('Добавить характеристики - да/нет: ') == 'да':
        f_key = input('Характеристика ->')
        f_val = input('Значение ->')
        fs[f_key] = f_val
    gs.append(tuple([cur, fs]))
    cur += 1

print('Набор товаров', gs)

for g in gs:
    for f_key, f_val in g[1].items():
        if f_key in a:
            if f_val not in a[f_key]:
                a[f_key].append(f_val)
        else:
         a[f_key] = [f_val]

print('Аналитика', a)
