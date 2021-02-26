class NotDigitError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return self.error


l = []

while True:
    a = input("Введите число или stop для выхода->")

    if a == "stop":
        break

    try:
        if not a.isdigit():
            raise NotDigitError(a + ' не число')
        l.append(int(a))
    except NotDigitError as e:
        print(e)

print('Введенный список->', l)
