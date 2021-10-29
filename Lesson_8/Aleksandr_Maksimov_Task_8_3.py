# даже не знаю как это комментировать

def type_logger(func):
    def type_printer(*args):
        answer = []
        for a in args:
            answer.append(f'{func.__name__}({a}: {type(a)})')
        print(', '.join(answer))
    return type_printer

@type_logger
def calc_cube(x):
   return x ** 3

# Список значений для распознавания
a = calc_cube(5, '6', 7, 8.5)