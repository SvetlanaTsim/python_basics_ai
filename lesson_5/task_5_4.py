"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
change_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('nums.txt', encoding='utf-8') as fr, open ('new_nums.txt', 'w', encoding='utf-8') as fa:
    for line in fr:
        for key, val in change_dict.items():
            if line.find(key) == 0:
                new_line = line.replace(key, val)
                fa.write(new_line)
