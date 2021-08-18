"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
 Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count
from itertools import cycle

#a
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

#б
# как я поняла, можно за пределами функции оставить список, так как он является константой
my_list = cycle([1, 2, 3, 4, 5])

def print_my_list(num):
    """Функция, которая печатает переданное количество элементов итератора my_list"""
    for i in range(int(num)):
        print(next(my_list))

print_my_list(num = input('Введите, сколько чисел из бесконечного списка 1-5 напечатать (натуральное число): '))
