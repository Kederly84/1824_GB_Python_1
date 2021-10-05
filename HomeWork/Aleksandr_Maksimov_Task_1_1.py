# задание №1

# Запрос ввода от пользователя в секундах
duration = int(input('Веди время в секундах'))

days = duration // 86400  # 86400 - это количество секунд в сутках, вычисляем кол-во суток
hours = (duration - days * 86400) // 3600  # 3600 количество секунд в часе, вычисляем кол-во часов
minutes = (duration - days * 86400 - hours * 3600) // 60  # Вычисляем кол-во минут
seconds = duration - days * 86400 - hours * 3600 - minutes * 60 # Вычисляем оставшиеся секунды

# Вывод информации в зависимости от данных, введенных пользователем
# без лишних сущностей

if duration >= 86400:
    print('Вы ввели', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
elif 3600 <= duration < 86400:
    print('Вы ввели', hours, 'час', minutes, 'мин', seconds, 'сек')
elif 60 <= duration < 3600:
    print('Вы ввели', minutes, 'мин', seconds, 'сек')
else:
    print('Вы ввели', duration, 'сек')






