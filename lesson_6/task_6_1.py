"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
 Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
 третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from itertools import cycle
from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = [(7, 'red'), (2, 'yellow'), (3,'green')]

    def run(self):
        i = 0
        for time, color in cycle(self.__color):
            print(color, f'ждем {time} сек.', sep='\n')
            sleep(time)
            i += 1
            # сделаю 3 показа
            if i >= 3:
                break


tr_light = TrafficLight()
tr_light.run()
