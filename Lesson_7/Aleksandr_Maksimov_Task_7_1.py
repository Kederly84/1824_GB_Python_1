# Импорт необходимых библиотек
import os

# Создание необходимых переменных
base_dir = 'my_project'
subfolders = ['settings', 'mainapp', 'adminapp', 'authapp']

def create_project(base, dirs):
    """Функция принимает на входе название основной папки и
    список из вложенных папок"""
    creation_base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), base)
    if not os.path.exists(creation_base_dir):
        os.mkdir(creation_base_dir)
    else:
        print(f'{base_dir} уже существует')
    for dir in dirs:
        creation_other_dirs = os.path.join(base, dir)
        if not os.path.exists(creation_other_dirs):
            os.mkdir(creation_other_dirs)
        else:
            print(f'{dir} уже существует')

# Запуск функции
start = create_project(base_dir, subfolders)