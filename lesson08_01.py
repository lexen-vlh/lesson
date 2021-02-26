class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd, self.mm, self.yyyy = self.extract(dd_mm_yyyy)

        if not self.validation(self.dd, self.mm, self.yyyy):
            print('Дата введена некорректно ' + str(dd_mm_yyyy))

    @classmethod
    def extract(cls, dd_mm_yyyy):
        l = []
        try:
            for i in dd_mm_yyyy.split('-'):
                l.append(int(i))
        except:
            print('Неверный формат ' + str(dd_mm_yyyy))
            return 0, 0, 0

        return l[0], l[1], l[2]

    @staticmethod
    def validation(dd, mm, yyyy):
        dd_in_mm = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if yyyy % 4 == 0 or (yyyy % 100 != 0 and yyyy % 400 == 0):
            dd_in_mm[2] = 29

        if mm < 1 or mm > 12:
            print('Неверный месяц')
            return False

        if dd < 1 or dd > dd_in_mm[mm]:
            print('Неверный день')
            return False

        return True

    def __str__(self):
        return 'Дата ' + str(self.dd) + '-' + str(self.mm) + '-' + str(self.yyyy)


date1 = Data('01-01-1990')
print(date1)

print('------------------------')

date2 = Data('29-02-1990')
print(date2)
