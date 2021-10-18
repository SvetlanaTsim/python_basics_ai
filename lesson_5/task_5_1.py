"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
#Вариант 1
with open('user_text.txt', 'w', encoding='utf-8') as f:
    user_t = 1
    while user_t:
        user_t = input('Введите текст для записи в файл, чтобы выйти оставьте пустую строку и нажмите Enter: ')
        f.write(user_t + '\n')

# #Вариант 2
# with open('user_text.txt', 'a', encoding='utf-8') as f:
#     while True:
#         user_t = input('Введите текст для записи в файл, чтобы выйти оставьте пустую строку и нажмите Enter: ')
#         if not user_t:
#             break
#         else:
#             f.write(user_t + '\n')
