# Уравнение вида kx + b = c дано в виде строки. Решить уровнение по формуле  x = (c - b)/k

import re

#пример строки уравнения
#str = '- 10x + 17 = - 25.8'
str = '17 = - 25.8 - 10x'

#находим, часть до знака равенства и после него
left_part, right_part = str.split('=')

#составляем регулярное выражение, которое найдет нам все числа
RE_NUMBER = re.compile(r'[-+ ]{0,}[0-9.x]{1,}')

left_nums = RE_NUMBER.findall(left_part)
right_nums = RE_NUMBER.findall(right_part)

#пишем функцию, которая будет решать уравнение
def decision(nums_part, other):
    """решает уравнение в вида  kx + b = c, данное в виде строки, поделенное на 2 части по знаку '='
    nums_part - та часть уравнения, где находится х, list
    other - та часть, где нет х, list
    """
    for el in nums_part:
        for letter in el:
            if letter == 'x':
                k = el.replace('x', '').replace(' ', '')
                if k == '-':
                    k = -1.0
                elif k == '+':
                    k = 1.0
                else:
                    k = float(k)
                nums_part.remove(el)
                if not nums_part:
                    b = 0
                else:
                    b = float(nums_part[0].replace(' ', ''))
                c = float(other[0].replace(' ', ''))
                return(f'Уравнение {k}x + {b} = {c}, x = {round((c - b)/k, 2)}')

#найдем в какой части х и решим уравнение
for i in left_part:
    if i == 'x':
        print(decision(left_nums, right_nums))
for i in right_part:
    if i == 'x':
        print(decision(right_nums, left_nums))