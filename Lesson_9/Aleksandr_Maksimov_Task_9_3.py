# Создание класса
class Worker:

    _income: dict = {'wage': 1000,
                     'bonus': 100}

    def __init__(self, name: str, surname: str, position: str):
        """Запрос аттирбутов при создании дочернего класса"""
        self.name = name
        self.surname = surname
        self.position = position


# Создание дочернего класса
class Position(Worker):

    def get_full_name(self):
        """Метод для вывода информации по работнику"""
        print(f'{self.name.title()} {self.surname.title()}')

    def get_total_income(self, seniority: int):
        """Метод для расчета дохода сотрудника за заданный период"""
        inc = seniority * sum(Position._income.values())
        return inc


# Создание экземпляра дочернего класса
a = Position('Александр', 'максимов', 'работник')
a.get_full_name()
# Вывод дохода на печать
print(a.get_total_income(5))
