# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce


def sum_of_list(text):
    my_list = text.split(' ')
    my_list = list(map(get_num, my_list))
    return sum(my_list)


def get_num(num):
    try:
        num = float(num)
        return num
    except:
        return 0


numbers = '10 23.4 1 8 7 4 17 3.2 1.5 5 7.63 8.11 9'

with open('txt_task_05.txt', 'w+', encoding='utf-8') as file:
    file.write(numbers + '\n')
    file.seek(0)
    print(f'Сумма всех чисел в файле = {sum_of_list(file.read())}')
