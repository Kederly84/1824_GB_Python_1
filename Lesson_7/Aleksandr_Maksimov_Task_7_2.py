# Импорт библиотек
import os

# Объявление переменной
structure = []

# Чтение структуры из yaml и преобразование данных в список списков с уровнями вложенности
with open('config.yaml', 'r', encoding='utf-8') as f:
    for row in f:
        a = row.split('-')
        structure.append([len(a[0]), a[-1][:-1]])

# Создаем корневую папку
creation_project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), structure[0][1])
if not os.path.exists(creation_project_dir):
    os.mkdir(creation_project_dir)
else:
    print(f'Директория {structure[0][1]} уже существует')


def some_maker(unit_name, unit_dir):
    """Функция принимает на входе название файла или папки и директорию где она должна быть.
    Затем определяет что это (файл или папка) и создает необходимое"""
    hello = 'Hello'
    unit_name = unit.split('.')
    if len(unit_name) > 1:
        with open(unit_dir, 'w', encoding='utf-8') as f:
            f.write(hello)
    else:
        if not os.path.exists(unit_dir):
            os.mkdir(unit_dir)
        else:
            print(f'Директория {unit_name} уже существует')

# Цикл для вызова функции
for i in range(len(structure)):
    level = structure[i][0]
    unit = structure[i][1]
    if level == 4:
        creation_dir_4 = os.path.join(creation_project_dir, unit)
        some_maker(unit, creation_dir_4)
    if level == 7:
        creation_dir_7 = os.path.join(creation_dir_4, unit)
        some_maker(unit, creation_dir_7)
    if level == 10:
        creation_dir_10 = os.path.join(creation_dir_7, unit)
        some_maker(unit, creation_dir_10)
    if level == 13:
        creation_dir_13 = os.path.join(creation_dir_10, unit)
        some_maker(unit, creation_dir_13)