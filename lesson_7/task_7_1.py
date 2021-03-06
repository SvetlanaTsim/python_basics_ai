'''
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, matrix):
        self.matrix= matrix

    def __str__(self):
        return ','.join(map(str, self.matrix)).replace(']', '\n').replace('[', '').replace(',', '')

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            for row1, row2 in zip(self.matrix, other.matrix):
                if len(row1) != len(row2):
                    return f'Длина рядов не равна, эти матрицы нельзя сложить'
            result = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.matrix, other.matrix)]
            return ','.join(map(str, result)).replace(']', '\n').replace('[', '').replace(',', '')
        else:
            return f'Количество рядов не равно, эти матрицы нельзя сложить'


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(m_1)
print(m_1 + m_2)