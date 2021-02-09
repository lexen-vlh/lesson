import json

with open('input05_07.txt', 'r', encoding='utf-8') as f:
    print('Содержимое файла input.txt->')
    print(f.read())

earnings = {}
avr_e = {}
sum_e = 0


with open('input05_07.txt', 'r', encoding='utf-8') as f:
    num = 0
    for i in f:
        name, form, earning, costs = i.split()
        earnings[name] = int(earning) - int(costs)

        if earnings.setdefault(name) >= 0:
            sum_e += earnings.setdefault(name)
            num += 1

    if num != 0:
        avr_e['average_profit'] = round(sum_e / num)

with open('output05_07.json', 'w+', encoding='utf-8') as js:
    json.dump(earnings, js)
    json.dump(avr_e, js)

with open('output05_07.json', 'r', encoding='utf-8') as f:
    print('Содержимое файла output.json->')
    print(f.read())
