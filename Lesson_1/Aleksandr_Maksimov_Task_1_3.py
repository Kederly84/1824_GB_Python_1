# задание №3

# Создание пустого списка
percent = []

# заполнение списка необходимыми значениями
for i in list(range(1, 101)):
    percent.append(i)

for i in range(len(percent)):
    number = list(str(percent[i]))
    if i == 0:
        print(percent[i], 'процент')
    if 1 <= i < 4:
        print(percent[i], 'процента')
    if i in range(4, 19):
        print(percent[i], 'процентов')
    if number[-1] == '1' and percent[i] > 19:
        print(percent[i], 'процент')
    if number[-1] == '0' and percent[i] > 19:
        print(percent[i], 'процентов')
    if int(number[-1]) in range(2, 5) and percent[i] > 19:
        print(percent[i], 'процента')
    if int(number[-1]) in range(5, 10) and percent[i] > 19:
        print(percent[i], 'процентов')
