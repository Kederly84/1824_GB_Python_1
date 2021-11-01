from abc import ABC, abstractmethod


# Создание родительского класса
class Stationery(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def draw(self):
        """Метод отрисовки"""
        print(f'Запуск отрисовки')


# Создание дочернего класса
class Pen(Stationery):
    def draw(self):
        """Переопределение родительского метода"""
        print(f'Я ручка. Я пишу')


# Создание дочернего класса
class Pencil(Stationery):
    def draw(self):
        """Переопределение родительского метода"""
        print(f'Я карандаш. Я сломался')


# Создание дочернего класса
class Handle(Stationery):
    def draw(self):
        """Переопределение родительского метода"""
        print(f'Я маркер. Я высох')


# Создание экземпляров классов
b = Pen('Pen')
c = Pencil('Pencil')
d = Handle('Handle')
# Вызов методов классов
Stationery.draw('Stationery')
b.draw()
c.draw()
d.draw()