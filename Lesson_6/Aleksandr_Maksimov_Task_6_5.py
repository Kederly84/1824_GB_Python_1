# Вынес функцию в отдельный файл, чтобы не загромождать данный.
# Честно не знаю зачем. Тут импорт функции из файла с основной магией
from utils import wording


def util(argv):
    """Функция, которая передает необходимые аргументы в исполняемый файл"""
    arg_1 = argv[-3]
    arg_2 = argv[-2]
    arg_3 = argv[-1]
    result = wording(arg_1, arg_2, arg_3)

if __name__ == '__main__':
    import sys

    exit(util(sys.argv))