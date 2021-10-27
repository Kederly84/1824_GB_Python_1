# даже не знаю как это комментировать

def val_checker(func):
    def wrapper(func_2):
        def second_wrapper(arg):
            if func(arg) is True:
                result = func_2(arg)
                print(result)
            else:
                msg = f'Wrong val: {arg}'
                raise ValueError(msg)
        return second_wrapper
    return wrapper

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

# Вызов функции
a = calc_cube(5)
