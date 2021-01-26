a = 10
b = 3.1415926
c = "Hello"
d = [1, 2, 3]
print(a)
print(b)
print(c)
print(d)

print('Введите три числа')
try:
    e, f, g = map(int, input().split())
    print('Вы ввели числа ', e, ', ', f, ', ', g)
except:
    print('Необходимо было вводить числа')

print('Введите пару строк')
h = input()
i = input()
print('Первая строка - ', h)
print('Вторая строка - ', i)