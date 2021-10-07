# Задача
task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Цикл для перебора элементов списка и приведения числовых данных к нужному формату
for i in range(len(task_list)):
    check = list(task_list[i])
    if check[-1].isdigit() == True and len(check) < 2:
        task_list[i] = str('0' + task_list[i])
    elif check[-1].isdigit() == True and len(check) >= 2 and check[0].isdigit() == False:
        task_list[i] = str(check[0] + '0' + check[-1])

# формирования вывода в нужном формате
message = ' '.join(task_list)

print(message)