# Создание родительского класса
class Stationery:
    title: str = 'Канцелярская принадлежность'
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
a = Stationery()
b = Pen()
c = Pencil()
d = Handle()
# Вызов методов классов
a.draw()
b.draw()
c.draw()
d.draw()