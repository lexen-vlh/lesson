class Road:
    _length = None
    _width = None

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, weight, thickness):
        return self._length * self._width * weight/1000 * thickness


a = Road(5000, 20)
print('Масса асфальта для дорожного покрытия 20м * 5000м * 25кг * 5см =', round(a.calc(25, 5)), 'т')
