# Создание класса
class Worker:
    name: str = 'Александр'
    surname: str = 'Максимов'
    position: str = 'Дворник'
    _income: dict = {'wage': 0,
                     'bonus': 0}

    def __init__(self, wage: int, bonus: int):
        """Запрос аттирбутов при создании дочернего класса"""
        self._income['wage'] = wage
        self._income['bonus'] = bonus


# Создание дочернего класса
class Position(Worker):

    def get_full_name(self):
        """Метод для вывода информации по работнику"""
        print(f'{Position.name} {Position.surname}')

    def get_total_income(self, seniority: int):
        """Метод для расчета дохода сотрудника за заданный период"""
        inc = seniority * (Position._income['wage'] + Position._income['bonus'])
        return inc


# Создание экземпляра дочернего класса
a = Position(1000, 100)
# Вывод дохода на печать
print(a.get_total_income(5))
