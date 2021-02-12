class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return self.name + ' поехала'

    def stop(self):
        return self.name + ' остановилась'

    def turn(self, direction):
        return self.name + ' повернула на' + direction

    def show_speed(self):
        return 'текущая скорость машины ' + self.name + ' ' + self.speed + ' км\ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'текущая скорость машины ' + self.name + ' ' + str(self.speed) + ' км\ч, вы превысили допустимый лимит в 60 км/ч'
        else:
            return 'текущая скорость машины ' + self.name + ' ' + str(self.speed) + ' км\ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'текущая скорость машины ' + self.name + ' ' + str(self.speed) + ' км\ч, вы превысили допустимый лимит в 40 км/ч'
        else:
            return 'текущая скорость машины ' + self.name + ' ' + str(self.speed) + ' км\ч'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def ispolice(self):
        if self.is_police:
            return self.name + ' полицейская машина'
        else:
            return self.name + ' не полицейская машина'


a = TownCar(10, 'зеленый', 'камаз', False)
b = SportCar(100, 'красная', 'феррари', False)
c = WorkCar(60, 'синий', 'гольф', False)
d = PoliceCar(50, 'белый', 'уаз', True)

print('TownCar -', a.show_speed())
print('SportCar - цвет машины', b.name, b.color)
print('WorkCar -', c.show_speed())
print('PoliceCar - это', d.ispolice())
