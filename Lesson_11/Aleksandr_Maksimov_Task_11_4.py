# Импорт необходимых классов
from utils import Warehouse, OfficeEq

# Создание классов наследников от родительского из utils
class Printer(OfficeEq):
    def __init__(self, seal: bool, quantity: int):
        self.seal = seal
        self.quantity = quantity
        OfficeEq.__init__(self, title='Принтер', color='белый')


class Scaner(OfficeEq):
    def __init__(self, scanning: bool, quantity: int):
        self.scanning = scanning
        self.quantity = quantity
        OfficeEq.__init__(self, title='Сканер', color='малиновый')


class Xerox(OfficeEq):
    def __init__(self, whatwecopy: str, quantity: int):
        self.whatwecopy = whatwecopy
        self.quantity = quantity
        OfficeEq.__init__(self, title='Ксерокс', color='желтый')


try:
    # Создаем экземпляры классов (коробки с техникой) и склад
    a = Xerox('бззз', 1)
    b = Printer(False, 3)
    c = Scaner(True, 2)
    e = Warehouse(10)
    # Перемещаем коробки на склад
    e.additem(a)
    e.additem(b)
    e.additem(c)
    # Проверяем что на складе
    print(e)
    # Создаем еще одну коробку с принтерами
    f = Printer(False, 5)
    # Перемещаем 2 принтера из коробки на склад
    f.move_to_warehouse(2)
    # Проверяем что стало на складе и что осталось в коробке
    print(e)
    print(f)
    # Выдаем со склада что то и проверяем что осталось на складе
    e.removeitem('Сканер', 1)
    print(e)
except Exception as err:
    print(err)
except ValueError as v:
    print(v)