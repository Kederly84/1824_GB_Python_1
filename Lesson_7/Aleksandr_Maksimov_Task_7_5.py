# Решение для задачи 7_4 и 7_5  Отдельно 7_4 писать не стал
# Импорт необходимых библиотек
import os
import ntpath

# Объявление необходимых переменных и создание словаря
control_size = 2 ** 10
files = {100: (0, []),
         250: (0, []),
         500: (0, []),
         750: (0, []),
         1000: (0, [])}
folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trash')

def dict_writer(file_path, position):
    """Функция на входе получает путь до файла и ключ для словаря
    Затем выделяет расширение и если оно отсутствуе в соответствующем ключе словаря
    дописывает его тудаб а также увеличивает счетчик файлов"""
    file_ext = ntpath.splitext(file_path)[-1]
    ext_list = files[position][1]
    if ext_list.count(file_ext) == 0:
        ext_list.append(file_ext)
    counter = files[position][0] + 1
    files[position] = (counter, ext_list)

# Цикл для перебора файлов и определения его позиции в словаре
for file in os.scandir(folder):
    if file.stat().st_size <= control_size * 100:
        dict_writer(file, 100)
    elif control_size * 100 < file.stat().st_size <= control_size * 250:
        dict_writer(file, 250)
    elif control_size * 250 < file.stat().st_size <= control_size * 500:
        dict_writer(file, 500)
    elif control_size * 500 < file.stat().st_size <= control_size * 750:
        dict_writer(file, 750)
    elif control_size * 750 < file.stat().st_size <= control_size * 1000:
        dict_writer(file, 1000)

# запись итогового словаря в json
file_dict = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dictionary.json')
with open(file_dict, 'w', encoding='utf-8') as f:
    for key, val in files.items():
        f.write(f'{key}: {val}\n')