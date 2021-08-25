'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
 speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать,
  что машина поехала, остановилась, повернула (куда).
  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
  Добавьте в базовый класс метод show_speed, который должен показывать
  текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
    #не совсем поняла, как сделать булевый атрибут, сделала так
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала!'

    def stop(self):
        return f'Машина {self.name} остановилась!'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превышаете скорость! Ваша скорость - {self.speed}'
        else:
            return f'Ваша скрость в рамках допустимых значений. Ваша скорость - {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превышаете скорость! Ваша скорость - {self.speed}'
        else:
            return f'Ваша скрость в рамках допустимых значений. Ваша скорость - {self.speed}'


class PoliceCar(Car):
    #сделала обязательным is_police
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if is_police == False:
            print('Это не полицейская машина!')


aston_martin = TownCar(120,'red','Aston Martin')
print(aston_martin.show_speed())
print(aston_martin.go())
print(aston_martin.stop())
print(aston_martin.turn('right'))
print(aston_martin.name)
lada_largus = WorkCar(50,'white','Lada')
print(lada_largus.show_speed())
toyota_caldina = PoliceCar(60,'blue', 'Toyota Caldina', is_police=True)
print(toyota_caldina.is_police)



