from abc import ABC, abstractmethod


# Создание абстрактного класса
class Clothes(ABC):
    def __init__(self, size: int):
        self.size = size

    @abstractmethod
    def quantity_of_fabric(self):
        """Определение абстрактного метода, который наследники будут переопределять"""
        pass


# Создание дочернего класса для пальто
class Coat(Clothes):

    @property
    def quantity_of_fabric(self):
        """Переопределение метода для расчета кол-ва ткани на пальто"""
        fabric = self.size / 6.5 + 0.5
        return fabric


# Создание дочернего класса для пиджака
class Dress(Clothes):

    @property
    def quantity_of_fabric(self):
        """Переопределение метода для расчета кол-ва ткани на пиджак"""
        fabric = self.size * 2 + 0.3
        return fabric


# Создание экземпляров классов
a = Coat(5)
b = Dress(5)
# Вывод результатов на печать
print(float('{:.2f}'.format(a.quantity_of_fabric)))
print(float('{:.2f}'.format(b.quantity_of_fabric)))
