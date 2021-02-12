class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки. ' + self.title


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки. ' + 'Pen - ' + self.title


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки. ' + 'Pencil - ' + self.title


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки. ' + 'Handle - ' + self.title


a = Pen('ручка')
b = Pencil('карандаш')
c = Handle('маркер')
print(a.draw())
print(b.draw())
print(c.draw())
