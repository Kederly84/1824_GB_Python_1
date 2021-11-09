# Импорт необходимых бибилиотек
import re


class Date:

    def __init__(self, date: str):
        self.date = date

    @staticmethod
    def validator(date):
        """Метод для валидации формата в котором передана дата"""
        re_date = re.split(r'[^0-9]+', date)
        if len(re_date) == 3 and 1 <= int(re_date[0]) <= 31 and 1 <= int(re_date[1]) <= 12 \
                and 1 <= int(re_date[2]) <= 2021:
            return re_date
        else:
            msg = 'Вы ввели дату не в том формате'
            raise ValueError(msg)

    @classmethod
    def int_giver(cls, param):
        """Метод возвращает числа из которых состоит дата"""
        answer = Date.validator(param)
        return answer

# вывод данных на экран
try:
    print(*Date.int_giver('26-03-1986'))
except ValueError as val:
    print(f'{val}')
