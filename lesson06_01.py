from time import sleep


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        times = [7, 2, 5]
        for i in range(0, 3):
            print('Горит->', TrafficLight.__color[i])
            sleep(times[i])


a = TrafficLight()
a.running()
