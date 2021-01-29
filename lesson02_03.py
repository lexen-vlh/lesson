s_list = ['зима', 'весна', 'лето', 'осень']
s_dict = {1:'зима', 2:'весна', 3:'лето', 4:'осень'}

print('Введите номер месяца')
try:
    m = int(input())
    if m in [12, 1, 2]:
        print('list -', s_list[0])
        print('dict -', s_dict.get(1))
    elif m in [3, 4, 5]:
        print('list -', s_list[1])
        print('dict -', s_dict.get(2))
    elif m in [6, 7, 8]:
        print('list -', s_list[2])
        print('dict -', s_dict.get(3))
    elif m in [9, 10, 11]:
        print('list -', s_list[3])
        print('dict -', s_dict.get(4))
    else:
        print('Такого месяца не существует')
except:
    print('Ошибка ввода')
