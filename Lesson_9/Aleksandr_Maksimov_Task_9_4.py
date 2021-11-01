# Импорт бибилиотеки
import random


# Создание родительского класса
class Car:

    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """Метод для старта"""
        self.speed = random.randint(10, 100)
        print(f'Машина едет со скоростью {self.speed} км/ч')

    def stop(self):
        """Метод для остановки"""
        self.speed = 0

    def turn(self, direction: str):
        """Метод для поворота и проверки его возможности )))"""
        if self.speed > 30:
            print(f'Убились мы на скорости {self.speed} км/ч')
        else:
            print(f'Машина повернула на {direction}')

    def show_speed(self):
        """Спидометр"""
        if self.speed == 0:
            print(f'А никто и никуда не едет. Стоим мы.')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч')


# Создание дочернего класса
class TownCar(Car):

    def show_speed(self):
        """Переопределение родительского метода"""
        if 0 < self.speed <= 60:
            print(f'Едем со скоростью {self.speed} км/ч')
        elif self.speed > 60:
            print(f'Притормози. Скрость {self.speed} км/ч')
        else:
            print(f'А никто и никуда не едет. Стоим мы.')


# Создание дочернего класса
class WorkCar(Car):

    def show_speed(self):
        """Переопределение родительского метода"""
        if 0 < self.speed <= 30:
            print(f'Едем со скоростью {self.speed} км/ч')
        elif self.speed > 30:
            print(f'Притормози. Скрость {self.speed} км/ч')
        else:
            print(f'А никто и никуда не едет. Стоим мы.')


# Создание дочернего класса
class SportCar(Car):
    color: str = 'фиолетовая'
    name: str = 'Ока'
    is_police: bool = False


# Создание дочернего класса
class PoliceCar(Car):
    color: str = 'белая'
    name: str = 'УАЗ'
    is_police: bool = True

    def show_speed(self):
        """Переопределение родительского метода"""
        print(f'Мы с мигалками! Скорость не важна!')

# Создание экземпляров классов и вызов методов
a = Car('зеленый', 'Жигули', False)
a.go()
a.show_speed()
a.turn('right')

b = TownCar('желтый', 'Ока', False)
b.stop()
b.go()
b.show_speed()

c = WorkCar('белый', 'Газель', False)
c.go()
c.show_speed()

d = SportCar('красный', 'Волга', False)
d.go()
d.stop()
d.show_speed()

e = PoliceCar('бело-синяя', 'УАЗ', True)
e.go()
e.show_speed()