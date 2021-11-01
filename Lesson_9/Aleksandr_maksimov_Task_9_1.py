# Импорт необходимых бибилиотек
import time

# Создание класса
class TrafficLight:
    __color: list = ['красный', 'желтый', 'зеленый']

    def running(self, working: int = 15):
        """Определение метода согласно условиям задачи"""
        while working > 1:
            if working > 8:
                print(f'Горит {TrafficLight.__color[0]} свет')
            elif 8 >= working > 6:
                print(f'Горит {TrafficLight.__color[1]} свет')
            else:
                print(f'Горит {TrafficLight.__color[2]} свет')
            time.sleep(1)
            working -= 1
        print('Светофорчик поломался')

# Создание экземпляра класса
a = TrafficLight()
# Вызов метода
a.running()