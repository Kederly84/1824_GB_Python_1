# Импорт стандартной библиотеки Python чтобы не сплитовать по несколько раз
import re

def show(argv):
    """Хтоническая фигня для вывода данных через интерфейс командной строки
    В качестве аргументов может принимать стартовое значение и конечное значение или только стартовое значение или
    ничего или стартовое и несуществующее в списке конечное значение и выводит результат согласно условиям задачи 6_6"""
    def start_pos(num):
        """Маленькая функция которая ищет стартовую позицию курсора для второго и третьего условия задачи 6_6"""
        pos_start = None
        with open('Storage/Storage.csv', 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                line_len = len(line)
                pos = re.split(': |\n', line)
                if pos[1] == num:
                    pos_start = f.tell() - line_len
                    break
                line = f.readline()
        if pos_start == None:
            print('Стартовое значение не найдено')
            sys.exit(1)
        else:
            return pos_start
    if 4 > len(argv) > 2:
        start = argv[-2]
        finish = argv[-1]
        with open('Storage/Storage.csv', 'r', encoding='utf-8') as f:
            f.seek(start_pos(start))
            line = f.readline()
            while line:
                pos = re.split(': |\n', line)
                if pos[1] != finish:
                    print(pos[1])
                elif pos[1] == finish:
                    print(pos[1])
                    break
                line = f.readline()
    elif len(argv) == 2:
        start = argv[-1]
        with open('Storage/Storage.csv', 'r', encoding='utf-8') as f:
            f.seek(start_pos(start))
            line = f.readline()
            while line:
                pos = re.split(': |\n', line)
                print(pos[1])
                line = f.readline()
    else:
        with open('Storage/Storage.csv', 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                pos = re.split(': |\n', line)
                print(pos[1])
                line = f.readline()

if __name__ == '__main__':
    import sys

    exit(show(sys.argv))