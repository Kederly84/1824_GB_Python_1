class Warehouse:
    """Класс склада оргтехники"""
    # Объявление необходимых атрибутов класса
    _content = {'Принтер': 0,
                'Сканер': 0,
                'Ксерокс': 0}
    _maxcapasity = 0

    def __init__(self, maxcapasity: int):
        self._maxcapasity = maxcapasity

    def additem(self, cls):
        """Метод добавления коробки на склад"""
        self.part_add(cls.title, cls.quantity)

    def removeitem(self, param_1: str, param_2: int):
        """Метод для выдачи со склада"""
        if type(param_1) is not str or type(param_2) is not int:
            msg = f'Не верный тип данных {param_1} или {param_2}. Должно быть param_1 - строка, param_2 - целое число.'
            raise ValueError(msg)
        else:
            if param_1.capitalize() in self._content.keys():
                if self._content[param_1] >= param_2:
                    a = self._content[param_1] - param_2
                    self._content[param_1] = a
                else:
                    msg = f'{param_1} нет на складе в достаточном количестве'
                    raise Exception(msg)
            else:
                msg = f'Техники с названием {param_1} нет на складе'
                raise Exception(msg)

    @staticmethod
    def part_add(param_1: str, param_2: int):
        """Метод для добавления на склад части коробки с техникой"""
        if (sum(Warehouse._content.values()) + param_2) >= Warehouse._maxcapasity:
            a = Warehouse._content[param_1] + param_2
            Warehouse._content[param_1] = a
        else:
            msg = f'Я не могу поместить это на склад. Количество {param_1} в размере {param_2} слишком большое'
            raise Exception(msg)

    def __str__(self):
        """Отчетность для контроля того что есть на складе"""
        return f'{self._content}'


class OfficeEq:
    """Класс оргтехники"""
    def __init__(self, title: str, color: str):
        self.title = title
        self.color = color

    def move_to_warehouse(self, par: int):
        """перемещение на склад части коробки"""
        if type(par) is int:
            if self.quantity >= par:
                self.quantity = self.quantity - par
                Warehouse.part_add(self.title, par)
            else:
                msg = f'Я не могу переместить {self.title} в количестве {par} на склад, т.к. в коробке их столько нет'
                raise Exception(msg)
        else:
            msg = f'Необходимо указыать перемещаемое кол-во как int, а не {type(par)}'
            raise Exception(msg)

    def __str__(self):
        """Перегрузка строкового метода для контроля того что осталось в коробке"""
        return f'{self.quantity}'
