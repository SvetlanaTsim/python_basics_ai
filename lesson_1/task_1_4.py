'''
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
user_num = int(input('Введите целое положительное число: '))

#число, чтобы сравнивать
test_num = 0
while user_num > 0:
    one_num = user_num % 10
    if one_num > test_num:
        test_num = one_num
    user_num //= 10

print(f'Самая большая цифра в числе - {test_num}')