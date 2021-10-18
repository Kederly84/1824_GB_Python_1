# Исходыне списки
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Александр', 'Василий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9A'
]

# Генератор, кривой но рабочий
def tutor_klass(a, b):
    def klass(n):
        if n < len(b):
            return b[n]
        else:
            return
    for i in range(len(a)):
        t_k = a[i], klass(i)
        yield t_k

# Вызов функции
answer = tutor_klass(tutors, klasses)
# Вывод ответа и проверка, что это действительно генератор
print(*answer)
print(type(answer))

