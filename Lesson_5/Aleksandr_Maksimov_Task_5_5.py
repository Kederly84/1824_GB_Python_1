# Исходный список
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 2, 2]
# Ответ для сверки
# result = [23, 1, 3, 10, 4, 11]

# Объявление всех необходимых списков и переменных
result = []
result_1 = []
tmp = set()

# Решение в лоб
for num in src:
    counter = src.count(num)
    if counter == 1:
        result.append(num)

# Решение с оптимизацией по быстродействию, для больших списков
for num in src:
    if num not in tmp:
        result_1.append(num)
        tmp.add(num)
    elif num in result_1:
        result_1.remove(num)

# Вывод результата
print(result)
print(result_1)