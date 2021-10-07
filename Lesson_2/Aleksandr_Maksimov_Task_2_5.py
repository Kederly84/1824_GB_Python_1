# задан список
price_list = [57.8, 46.54, 97, 34.3, 35.36, 84, 42.08, 42.10, 43, 44.15, 58, 7.1]

# объявление необходимых переменных
message_1 = ''
message_2 = ''

# цикл для перебора элементов списка с приведением их к строковому типу
# разделению по точке на рубли и копейки
# и приведение данных к указанному формату
for i in range(len(price_list)):
    price = str(price_list[i]).split('.')
    if len(price) > 1:
        item = (f'{price[0].zfill(2)} руб {price[1].ljust(2,"0")} коп')
    else:
        item = (f'{price[0].zfill(2)} руб 00 коп')
    message_1 += item
    message_1 += ', '

# вывод данных
print(message_1)

# сортировка списка и вывод id  полученных списков для доказательства,
# что это один и тот же объект
print(id(price_list))
price_list.sort()
print(id(price_list))

for i in range(len(price_list)):
    price = str(price_list[i]).split('.')
    if len(price) > 1:
        item = (f'{price[0].zfill(2)} руб {price[1].ljust(2,"0")} коп')
    else:
        item = (f'{price[0].zfill(2)} руб 00 коп')
    message_2 += item
    message_2 += ', '

print(message_2)

# обратная сортировка списка (по убыванию) и доказательство,
# что это другой список через вывод id списка
reverse_sorted_list = sorted(price_list, reverse=True)
print(reverse_sorted_list)
print(id(reverse_sorted_list))

# вывод 5 первых позиций
message_3 = message_2.split(',')
message_3 = message_3[0:6]
message_3 = ', '.join(message_3)
print(str(message_3))







