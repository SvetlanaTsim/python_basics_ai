"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('user_text.txt') as f:
    line_count = 0
    file_dict = {}
    for line in f:
        line_count+=1
        newline = line.strip()
        #проверка,чтобы убрать запятые и т.д.
        for i in line:
            if i == '.' or i == ':' or i == ',' or i == ';' or i == '!' or i == '?':
                newline = line.replace(i, '').strip()
        file_dict[line_count] =len(newline.split())
print(f'В файле строк - {line_count}, количество слов в каждой строке: {file_dict}')
