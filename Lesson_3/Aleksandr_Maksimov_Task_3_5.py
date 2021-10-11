# Импортируем необходимые библиотеки
from random import choice

# Исходные списки из задания
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# Запрос ввода кол-ва шуток от пользователя
number_of_jokes = int(input('Введи кол-во шуток которое хочешь получить. От одного до пяти: '))

# Проверка - сможет ли программа сгенерировать необходимое пользователю кол-во шуток.
if number_of_jokes > len(nouns):
    print('Я не знаю столько шуток')
else:
    def get_jokes(n):
        """Функция на входе получает от пользователя число и возвращает по одному слову из каждого заданного списка"""
        jokes_list = []
        used_words = []
        i = 0
        def uniq_word(word, list):
            """Функция получает на входе слово и проверяет его вхождения в список уже использованных слов.
            Если слово есть в списке - генерируется новое слово"""
            while word in used_words:
                word = choice(list)
            else:
                used_words.append(word)
            return word
        while i < n:
            i += 1
            first_word = uniq_word(choice(nouns), nouns)
            second_word = uniq_word(choice(adverbs), adverbs)
            last_word = uniq_word(choice(adjectives), adjectives)
            jokes_list.append(f'{first_word} {second_word} {last_word}')
        return jokes_list
    # Вызов функции
    joke = get_jokes(number_of_jokes)
    # вывод результата
    print(joke)
