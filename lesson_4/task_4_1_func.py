"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
 заработной платы сотрудника. В расчете необходимо использовать формулу:
 (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
 значений необходимо запускать скрипт с параметрами.
"""
import sys
from decimal import Decimal

user_hours, user_earning_per_hour, user_bonus = sys.argv[1], sys.argv[2], sys.argv[3]
def salary_count(hours, earning_per_hour, bonus):
    return f'Расчет заработной платы сотрудника следующий: (выработка в часах {hours} * ставка в час {earning_per_hour}) ' \
           f'+ премия {bonus} = {round((Decimal(hours) * Decimal(earning_per_hour)) + Decimal(bonus), 2)}'

print(salary_count(user_hours, user_earning_per_hour, user_bonus))
