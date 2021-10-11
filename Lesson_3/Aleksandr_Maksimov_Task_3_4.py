# Список имен и фамилий
names = ['Александр Максимов', 'Екатерина Максимова', 'Игорь Белов', 'Владимир Борисов', 'Василий Беликов',
         'Алексей Митин', 'Екатерина Карогина', 'Екатерина Артамонова', 'Анастасия Богданова', 'Виктория Захарова',
         'Руслан Ходырев', 'Дмитрий Долгов', 'Алексей Клыков', 'Ирина Метелкина', 'Юлия Рубайло']

# Функция формирующая из списка словарь с вложенными словарями, согласно условию задания
def thesaurus_adv(lists):
    users = {}
    for i in range(len(lists)):
        words = lists[i].split(' ')
        if words[1][:1] not in users.keys():
            users[f'{words[1][:1]}'] = {f'{words[0][:1]}': [lists[i]]}
        else:
            second_word = users[words[1][:1]]
            if words[0][:1] not in second_word.keys():
                second_word[f'{words[0][:1]}'] = [lists[i]]
            else:
                elem = second_word[f'{words[0][:1]}']
                elem.append(lists[i])
                second_word[f'{words[0][:1]}'] = elem
    return users

# Вызов функции
wording = thesaurus_adv(names)

# вывод результата
print(wording)



