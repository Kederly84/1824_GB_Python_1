
def wording(file_1, file_2):
    """Функция возвращающая набор из Фамилий Имен Отчеств и хобби
    В качестве контейнера для хранения значений выбрано множество,
    т.к. оно сохраняет только уникальные значения и занимет меньше объема в памяти"""
    words = set()
    with open(file_1, 'r', encoding='utf-8') as f:
        for row_1 in f:
            row_1 = row_1[:-1].split(',')
            for _ in row_1:
                words.add(_)
    with open(file_2, 'r', encoding='utf-8') as f_2:
        for row_2 in f_2:
            row_2 = row_2[:-1].split(',')
            for _ in row_2:
                words.add(_)
    return words

# Вызов функции
result = wording('FIO/FIO.csv', 'Hobby/Hobby.csv')
# Вывод результата на печать
print(result)