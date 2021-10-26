# Т.к. писать копировщик файлов из одной папки в другую не интересно я добавил поиск
# нужной папки в проекте из задания 7_2 (там их 2 templates и в каждойй вложено что то свое)
# и копирование содержимого в нужное место
# Импорт необходимых бибилиотек
import os
import shutil

# Объявление/создание переменных
project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'my_project')
finder = os.walk(project_dir)
work_dir = []
# Простой поиск
for i in finder:
    if i.count(['templates']) > 0:
        work_dir.append(os.path.join(i[0], i[1][0]))
# Это на случай если нужной папки нет
if len(work_dir) == 0:
    print('Директория не найдена')

# Обходим копируем
counter = 0
for dir in work_dir:
    scan = os.walk(dir)
    for some_paths in scan:
        if len(some_paths[-1]) >= 1:
            counter += 1
            sought_files = some_paths[-1]
            for needed_file in sought_files:
                copied_file_path = os.path.join(some_paths[0], needed_file)
                copy_file_path = os.path.join(dir, needed_file)
                with open(copied_file_path, 'r', encoding='utf-8') as src:
                    with open(copy_file_path, 'w', encoding='utf-8') as dst:
                        shutil.copyfileobj(src, dst)

# Предупреждениеб если файлов нет
if counter == 0:
    print('Files not found')