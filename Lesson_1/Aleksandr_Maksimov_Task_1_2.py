# задание №2

# Объявление всех необходимых переменных и создание списков
numbers = []
seven_numbers = []
counter = 0
total_sum = 0
seventeen_sum = 0

# Создание списка из кубов чисел от 1 до 1000
for i in list(range(1, 1001, 2)):
    i = i ** 3
    numbers.append(i)

# Вывод списка
print(numbers)

# Создание списка чисел сумма цифр которых делится без остатка на 7
for i in range(len(numbers)):
    number = list(str((numbers[i])))
    y = 0
    summary = 0
    while y < len(number):
        summary += int(number[y])
        y += 1
        if y == len(number) and summary % 7 == 0:
            seven_numbers.append(numbers[i])

# Вывод списка чисел, где сумма цифр делится на 7 без остатка
print(seven_numbers)

# Вычисление суммы всех чисел, сумма цифр которых делится на 7 без остатка
while counter < len(seven_numbers):
    total_sum += seven_numbers[counter]
    counter += 1

# Вывод полученной суммы
print(total_sum)

# Расчет суммы чисел первоначального списка numbers,
# где каждый элемент списка увеличен на 17
# без создания нового промежуточного списка
for i in range(len(numbers)):
    check = numbers[i] + 17
    number = list(str((check)))
    b = 0
    summary = 0
    while b < len(number):
        summary += int(number[b])
        b += 1
        if b == len(number) and summary % 7 == 0:
            seventeen_sum += check

# Вывод суммы чисел первоначального массива, где каждое число увеличено на 17
# и суммаа цифр данного числа кратна 7
print(seventeen_sum)

