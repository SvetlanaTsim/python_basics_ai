"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

#создаем пустые словари
firms_dict = {}
profit_dict = {}

#заранее создадим ключ 'average_profit', чтобы он был на первом месте
profit_dict.setdefault('average_profit', 0)

with open ('firms.txt', encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        firms_dict[line_list[0]] = int(line_list[2]) - int(line_list[3])

#найдем сумму всех доходов и количество фирм
profit_sum = sum(firms_dict.values())
firm_number = len(firms_dict)

# в цикле отнимем данные убыточных фирм и занесем их в словать по прибыли
for key, value in firms_dict.items():
    if value < 0:
        profit_sum -= value
        firm_number -= 1
        profit_dict[key] = value

profit_dict['average_profit'] = profit_sum / firm_number

#создаем итоговый список
out_list = [firms_dict, profit_dict]
print(out_list)

#загрузим в файл
with open('firm_data.json', 'w') as fj:
    json.dump(out_list, fj)
