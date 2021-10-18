"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый — с декоратором @classmethod. Он должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных.
"""

class Date:
    #создадим переменную класса, чтобы работало без экземпляра
    date = '31-08-2021'

    def __init__(self, new_date):
        Date.date = new_date

    @classmethod
    def date_to_number(cls):
        day, month, year = cls.date.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def valid_data():
        day, month, year = Date.date_to_number()
        if month < 1 or month > 12:
            return 'Wrong month'
        #для високосного не делала
        if not ((day >= 1 and day <= 30 and month in [4, 6, 9, 11]) or (day >= 1
            and day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]) or (day >= 1 and day <= 28 and month == 2)):
            return 'Wrong day'
        if not (year >= 1 and year <= 2021):
            return 'Wrong year'
        return 'Date is alright'



my_date = Date('30-02-2021')
print(Date.date_to_number())
print(Date.valid_data())
