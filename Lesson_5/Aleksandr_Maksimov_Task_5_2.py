# Запрос числа
n = input('Введите число n: ')

# Защита от дурака
counter = 0
while counter < 5:
    counter += 1
    if n.isdigit() == True:
        n = int(n)
        nums_gen = (num for num in range(1, n + 1, 2)) # ГЕНЕРААААТООООР!!!! ))))
        print(*nums_gen, sep=' ')
        print(type(nums_gen))
        break
    else:
        n = input('Введите число n: ')
else:
    print('Ничего. В другой раз повезет.')