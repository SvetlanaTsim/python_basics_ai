"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой!')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом!')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером!')

item_1 = Stationery('item_1')
item_1.draw()
pen_1 = Pen('pen_1')
pen_1.draw()
pencil_1 = Pencil('pencil_1')
pencil_1.draw()
handle_1 = Handle('handle_1')
handle_1.draw()