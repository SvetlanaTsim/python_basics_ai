"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def user_data(**kwargs):
    out_str= ''
    for key, val in kwargs.items():
        out_str += f'{key}: {val}; '
    return out_str

print(user_data(name='John', surname = 'Smith', bith=1987, age=33, city='London', email='john@mail.ru',
                phone=89145235325))
