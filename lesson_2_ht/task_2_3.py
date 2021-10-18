"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
# через list
season_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
user_m = input('Введите месяц (целое число от 1 до 12): ')
while not user_m.isdigit():
    user_m = input('Ошибка ввода! Введите месяц (целое число от 1 до 12): ')
while int(user_m) not in season_list:
    user_m = input('Ошибка ввода! Введите месяц (целое число от 1 до 12): ')

if int(user_m) in season_list[0:3]:
    print('Время года - зима!')
elif int(user_m) in season_list[3:6]:
    print('Время года - весна!')
elif int(user_m)  in season_list[6:9]:
    print('Время года - лето!')
elif int(user_m) in season_list[9:12]:
    print('Время года - осень!')

#через dict, проверки те же оставим
season_dict ={
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

for key, val in season_dict.items():
    if int(user_m) in val:
        print(f'Время года - {key}!')
