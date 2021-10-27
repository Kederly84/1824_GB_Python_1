# Импорт необходимых библиотек
import re

# Решение написано точно с ошибками и точно не правильно,
# НО оно работает и позволяет получить IPv6 адреса, которые есть в файле.
# И, главное, оно РАБОТАЕТ!!! ))))
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for row in f:
        stroke = re.split('--|"|\s', row)
        parsed_raw = stroke[0], stroke[3][1:] + ' ' + stroke[4][:-1], stroke[6], stroke[7], stroke[10], stroke[11]
        print(parsed_raw)
