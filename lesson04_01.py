from sys import argv

try:
    f_name, hours, rate, prem = argv
    print('Заработная плата', (float(hours) * float(rate) + float(prem)))
except:
    print('Невернный ввод')
