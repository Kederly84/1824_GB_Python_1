# Запись данныех в файл для задачи 6_6

def write(argv):
    """Функция для записи данных в файл через интерфейс командной строки.
    В результате ее работы получаем пронумерованный список значений в формате csv согласно условиям задачи"""
    arg = argv[-1]
    if arg == 'add_sale.py':
        print('Задайте число которое необходимо сохранить')
    else:
        with open('Storage/Storage.csv', 'a+', encoding='utf-8') as f:
            str_num = 1
            f.seek(0)
            line = f.readline()
            while line:
                str_num += 1
                line = f.readline()
            f.write(f'{str_num}: {arg}\n')

if __name__ == '__main__':
    import sys

    exit(write(sys.argv))