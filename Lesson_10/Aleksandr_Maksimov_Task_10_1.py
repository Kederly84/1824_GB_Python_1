# Создание класса
class Matrix:
    def __init__(self, matr: list):
        """Конструктор класса, принимающий матрицы"""
        self.matr = matr

    def __str__(self):
        """Перегрузка строкового метода"""
        matrix = ''
        for i in self.matr:
            matrix += f'{" ".join(map(str, i))}\n'
        return matrix

    def __add__(self, other):
        """Перегрузка метода сложения"""
        # Простое сравнение 2х матриц. Т.к. матрица это по факту таблица,
        # то проверяю только совпадение кол-ва строк и столбцов.
        # И проверка список ли вообще скормили методу.
        if len(self.matr) == len(other.matr) and len(self.matr[0]) == len(other.matr[0]) \
                and isinstance(self.matr, list) and isinstance(other.matr, list):
            # Поэлементное сложение
            result = [[self.matr[i][j] + other.matr[i][j]
                       for j in range(len(self.matr[0]))] for i in range(len(self.matr))]
        else:
            # Вызов ошибки на случай, если что то пошло не так.
            msg = f'Размеры матриц не совпадают или это вообще не матрицы'
            raise ValueError(msg)
        return result


# Создание экземплярова класса
a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Вывод результата перегрузки строкового метода
print(a)
print(b)
# Вывод результата сложения в заданном формате без скобок и запятых согласно условию задачи
for _ in (a+b):
    print(*_)
