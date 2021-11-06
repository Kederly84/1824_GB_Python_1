# Создание класса исключения для деления на 0
class DivErr(ZeroDivisionError):
    def __init__(self, txt: str):
        self.txt = txt


# Запрос чисел от пользователя
dividend = input('Введите делимое: ')
divisor = input('Введите делитель: ')
# Вывод данных на экран
try:
    dividend = int(dividend)
    divisor = int(divisor)
    if divisor == 0:
        raise DivErr('На ноль делить нельзя')
except ValueError:
    print('То что вы ввели не число')
except DivErr as e:
    print(e)
else:
    print(dividend / divisor)
