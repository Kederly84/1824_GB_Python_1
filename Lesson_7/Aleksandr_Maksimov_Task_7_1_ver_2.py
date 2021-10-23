# Вторая реализация первого задания. Оно такое же как и первое, но с исключениями
import os

base_dir = 'my_project'
subfolders = ['settings', 'mainapp', 'adminapp', 'authapp']

def create_project(base, dirs):
    creation_base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), base)
    try:
        os.mkdir(creation_base_dir)
    except FileExistsError as f:
        print(f'FileExistsError: {f}')
    for dir in dirs:
        try:
            creation_other_dirs = os.path.join(base, dir)
            os.mkdir(creation_other_dirs)
        except FileExistsError as e:
            print(f'FileExistsError: {e}')

start = create_project(base_dir, subfolders)