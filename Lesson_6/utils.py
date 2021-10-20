# Импорт необходимых библиотек
import sys

def wording(file_1, file_2, file_3):
    """Функция для задачи 6_5. Принимает в качестве аргументов путь к исходным файлам и файлу
    куда нужно вывести данные. Решение задачи аналогично 6_3"""
    users = []
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
        if n < len(hobby):
            return hobby[n]
        else:
            return
    for i in range(len(usr)):
        users.append(f'{usr[i]}: {hobbies(i)}\n')
    with open(file_3, 'w', encoding='utf-8') as f_3:
        f_3.writelines(users)
