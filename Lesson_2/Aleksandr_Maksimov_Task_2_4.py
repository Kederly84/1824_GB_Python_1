# заданный список
task_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# вывод данных в нужном формате
for i in range(len(task_list)):
    list_answer = task_list[i].split(' ')
    print('Привет, ' + list_answer[-1].capitalize() + '!')