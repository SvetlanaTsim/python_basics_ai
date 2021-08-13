"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""
def devision_func (a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return 'Деление на ноль недопустимо'
    else:
        return round(result, 2)

num_1, num_2 = map(float,input('Введите 2 числа через пробел: ').split())
print(f'Результат деления чисел: {devision_func(num_1, num_2)}')
