
def show(argv):
    """Функция для решения задачи 7. В качестве аргумента принимает номер позиции и новое значение.
    Затем построчно читает файл, заменяет нужное значение и переписывает файл построчно."""
    arg = argv[-2]
    check = int(arg)
    num = argv[-1]
    finish_list = []
    with open('Storage/Storage.csv', 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            finish_list.append(line)
            line = f.readline()
    if check > len(finish_list):
        print('Введеный номер не найден в списке')
        sys.exit(1)
    else:
        finish_list[check - 1] = f'{arg}: {num}\n'
        with open('Storage/Storage.csv', 'w', encoding='utf-8') as f:
            f.writelines(finish_list)

if __name__ == '__main__':
    import sys

    exit(show(sys.argv))
