# Создание класса
class Road:
    _lenght: int = 0
    _width: int = 0
    # Определение необходимых атрибутов при создании экземпляра класса
    def __init__(self, lenght: int, widht: int):
        Road._lenght = lenght
        Road._width = widht

    def mass(self, coating_thickness: int):
        """Метод для расчета массы асфальта"""
        mass_of_layer = 25
        total_mass = int((Road._width * Road._lenght * mass_of_layer * coating_thickness) / 1000)
        return total_mass

# Создание экземпляра класса
a = Road(5000, 20)
# Вызов метода и вывод результата на печать
print(f'Масса асфальта {a.mass(5)} тонн')
