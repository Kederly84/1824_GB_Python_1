# Импорт необходимых библиотек
import re


def email_parse(mail):
    """Функция для валидации адреса электронной почты. Точно не предусмотрел ситуацию,
    ели будет указан домен в имени пользователя, например vasya.com@gmail.com"""
    user_info = {'username': None,
                 'domain': None}
    re_check = re.compile(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$')
    if re_check.match(mail) is not None:
        user_info['username'] = mail.split('@')[0]
        user_info['domain'] = mail.split('@')[1]
        print(user_info)
    else:
        msg = f'wrong email: {mail}'
        raise ValueError(msg)

# Список адресов для проверки и вызов функции для валидации адреса
emails = ['aleksandr.maksimov@gmail.com', 'vasya@mail.com', 'petya@yandex.ru', 'grisha@inbox.ru', 'gosha@gb.ru']
for email in emails:
    email_parse(email)