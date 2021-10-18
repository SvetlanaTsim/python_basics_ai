"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
with open('salaries.txt', encoding='utf-8') as f:
    sal_dict = {}
    for line in f:
        dict_data = line.strip().split()
        sal_dict[dict_data[0]] = float(dict_data[1])

small_sal = []
for key, val in sal_dict.items():
    if val < 20000:
        small_sal.append(key)

print(f'зп меньше 20000 у сотрудников {small_sal}')
print(f'средний размер доходов сотрудников {sum(sal_dict.values())/len(sal_dict.values())}')
