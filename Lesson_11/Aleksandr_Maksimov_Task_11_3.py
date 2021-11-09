# Создание класса исключения
class ValErr(ValueError):

    def __init__(self, txt: str):
        self.txt = txt


# Запрос данных от пользователя
d = input('Введи число и скоро получишь сюрприз: ')
a = []

# Цикл запроса данных от пользователя
while d != 'stop':
    try:
        if not d.isdigit():
            raise ValErr('Это не число')
        else:
            d = int(d)
            a.append(d)
    except ValErr as e:
        print(e)
    print(a)
    d = input('Введи число и скоро получишь сюрприз: ')
