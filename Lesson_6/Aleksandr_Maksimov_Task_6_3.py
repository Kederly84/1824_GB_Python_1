# Импорт необходимых библиотек
import sys

def wording(file_1, file_2):
    """Функция для получения словаря с ФИО в качестве ключей
    и хобби как значений"""
    users = {}
    usr = []
    hobby = []
    with open(file_1, 'r', encoding='utf-8') as f:
        for row_1 in f:
            usr.append(row_1[:-1])
    with open(file_2, 'r', encoding='utf-8') as f_2:
        for row_2 in f_2:
            hobby.append(row_2[:-1])
    if len(usr) < len(hobby):
        sys.exit(1)
    def hobbies(n):
        """Функция возвращающая None в случае, если хобби меньше чем ФИО"""
        if n < len(hobby):
            return hobby[n]
        else:
            return
    for i in range(len(usr)):
        users[usr[i]] = hobbies(i)
    return users

# Вызов функции. Файлы изначально разнесены по папкам для выполнения заданий со звездочкой.
result = wording('FIO/FIO.csv', 'Hobby/Hobby.csv')
# Вывод результата на печать.
print(result)