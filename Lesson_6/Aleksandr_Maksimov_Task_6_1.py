# Импорт стандартной библиотеки Python чтобы не сплитовать по несколько раз
import re


# Объявление необходимых переменных
users = []
ip = []
tmp = set()
unique_ip = []

# Чтение файла и формирование списка в заданном формате
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for row in f:
        stroke = re.split('--|"| ', row)
        user = stroke[0], stroke[6], stroke[7]
        users.append(user)
        ip.append(stroke[0])

# Небольшая оптимизация по быстродействию
# и памяти для более быстрого поиска спамера
for _ in ip:
    if _ not in tmp:
        unique_ip.append(_)
        tmp.add(_)

# Поиск спамера
counter = ip.count(unique_ip[0])
adress = unique_ip[0]
for i in unique_ip:
    if ip.count(i) > counter:
        counter = ip.count(i)
        adress = i

# Вывод результатов
print(users)
print(f'Спамер {adress}, количество запросов {counter}')
