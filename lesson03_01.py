def division(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "ошибка деления на ноль"
    except:
        return "неверный ввод"

print('Результат деления -', division(input('a->'), input('b->')))
