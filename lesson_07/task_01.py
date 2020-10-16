# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, list_for_matrix):
        self.matrix = list_for_matrix

    def __str__(self):
        # pass
        return '\n'.join(' '.join(map(str, i)) for i in self.matrix) + '\n'

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            new_matrix = []
            for i, j in zip(self.matrix, other.matrix):
                new_matrix.append([num1 + num2 for num1, num2 in zip(i, j)])
            return Matrix(new_matrix)
        else:
            print('Матрицы разного размера. Сложение невозможно.')
            return None


matrix_1 = Matrix([[1, 2, 3], [5, 4, 3], [6, 5, 4]])
matrix_2 = Matrix([[3, 5, 1], [1, 3, 6], [2, 0, 1]])
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1+matrix_2
print(matrix_3)

matrix_4 = Matrix([[3, 5, 1], [1, 3, 6], [2, 0, 1], [2, 3, 1]])
print(matrix_1 + matrix_4)
