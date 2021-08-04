"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
 запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

num = 1
num_f = 1.1
city = 'Владивосток'
print(num, type(num), num_f, type(num_f), city, type(city), sep='\n')
user_num = int(input('Введите целое число: '))
user_fl = float(input('Введите дробное число: '))
user_name = input('Введите Ваше имя: ')
user_color = input('Введите Ваш любимый цвет: ')
print(user_num, type(user_num), user_fl, type(user_fl), user_name, type(user_name), user_color, type(user_color),
      sep='\n')
