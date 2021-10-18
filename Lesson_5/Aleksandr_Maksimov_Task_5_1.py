# Запрос ввода числа от пользователя
n = input('Введите число n: ')

# Генератор с yield
def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i

# Примитивная защита от дурака и вызов генератора
counter = 0
while counter < 5:
    counter += 1
    if n.isdigit() == True:
        n = int(n)
        answer = odd_nums(n)
        print(*answer, sep=' ')
        print(type(answer))
        break
    else:
        n = input('Введите число n: ')
else:
    print('Ничего. В другой раз повезет.')


