# Импорт бибилиотеки
import random


# Создание родительского класса
class Car:
    speed: int = 0
    color: str = 'red'
    name: str = 'Запорожец'
    is_police: bool = False

    def go(self):
        """Метод для старта"""
        Car.speed = random.randint(10, 100)
        print(f'Машина едет со скоростью {Car.speed} км/ч')

    def stop(self):
        """Метод для остановки"""
        Car.speed = 0

    def turn(self, direction: str):
        """Метод для поворота и проверки его возможности )))"""
        if Car.speed > 30:
            print(f'Убились мы на скорости {Car.speed} км/ч')
        else:
            print(f'Машина повернула на {direction}')

    def show_speed(self):
        """Спидометр"""
        if Car.speed == 0:
            print(f'А никто и никуда не едет. Стоим мы.')
        else:
            print(f'Скорость автомобиля {Car.speed} км/ч')


# Создание дочернего класса
class TownCar(Car):
    color: str = 'зеленая'
    name: str = 'Жигули'
    is_police: bool = False

    def show_speed(self):
        """Переопределение родительского метода"""
        if 0 < TownCar.speed <= 60:
            print(f'Едем со скоростью {TownCar.speed} км/ч')
        elif TownCar.speed > 60:
            print(f'Притормози. Скрость {TownCar.speed} км/ч')
        else:
            print(f'А никто и никуда не едет. Стоим мы.')


# Создание дочернего класса
class WorkCar(Car):
    color: str = 'Синяя'
    name: str = 'Газель'
    is_police: bool = False

    def show_speed(self):
        """Переопределение родительского метода"""
        if 0 < WorkCar.speed <= 30:
            print(f'Едем со скоростью {WorkCar.speed} км/ч')
        elif WorkCar.speed > 30:
            print(f'Притормози. Скрость {WorkCar.speed} км/ч')
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
a = Car()
a.go()
a.turn('right')

b = TownCar()
b.go()
b.show_speed()

c = WorkCar()
c.go()
c.show_speed()

d = SportCar()
d.go()
d.stop()
d.show_speed()

e = PoliceCar()
e.go()
e.show_speed()