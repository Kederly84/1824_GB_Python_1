# Создаем класс
class Cage:

    def __init__(self, cell: int):
        """Конструктор кдасса"""
        self.cell = cell

    def __add__(self, other):
        """Перегрузка сложения"""
        if isinstance(self.cell, int) and isinstance(other.cell, int):
            cells = self.cell + other.cell
        else:
            cells = f'Нельзя выполнить сложение'
        return cells

    def __sub__(self, other):
        """Перегрузка вычитания с проверкой условия согласно заданию"""
        if isinstance(self.cell, int) and isinstance(other.cell, int) and self.cell > other.cell:
            cells = self.cell - other.cell
        else:
            cells = f'Нельзя выполнить вычитание'
        return cells

    def __mul__(self, other):
        """Перегрузка умножения"""
        if isinstance(self.cell, int) and isinstance(other.cell, int):
            cells = self.cell * other.cell
        else:
            cells = f'Нельзя выполнить умножение'
        return cells

    def __floordiv__(self, other):
        """Перегрузка целочисленного деления"""
        if isinstance(self.cell, int) and isinstance(other.cell, int) and other.cell > 0:
            cells = self.cell // other.cell
        else:
            cells = f'Нельзя выполнить деление'
        return cells

    def __truediv__(self, other):
        """Перегрузка деления"""
        if isinstance(self.cell, int) and isinstance(other.cell, int) and other.cell > 0:
            cells = self.cell / other.cell
        else:
            cells = f'Нельзя выполнить деление'
        return cells

    def make_order(self, cell_size: int):
        """Определенин метода для организации ячеек клетки с запросом кол-ва ячеек в ряду"""
        if self.cell <= cell_size:
            result = f"{'*' * self.cell}"
        else:
            full_cells = self.cell // cell_size
            other_cells = self.cell % cell_size
            result = (f'{"*" * cell_size}\n' * full_cells) + ("*" * other_cells)
        return result


# Создание экземпляров классов
a = Cage(13)
b = Cage(6)
c = Cage(a + b)
# Вывод результатов работы всех методов
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a / b)
print(c.make_order(5))
