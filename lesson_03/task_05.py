# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
# вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def sum_of_list(text):
    my_list = text.split(' ')
    # my_list = list(filter(is_num, my_list))
    my_list = list(map(get_num, my_list))
    a = sum(my_list)
    return a


def get_num(num):
    try:
        num = float(num)
        return num
    except:
        return 0

# def is_num(num):
#     try:
#         float(num)
#         return True
#     except:
#         return False


sum_of_numbers = 0
while True:
    input_list = input('Введите строку с числами разделенными пробелами (для выхода введите "Q"): ')
    input_list = input_list.upper()
    if input_list == 'Q':
        print('Вывод завершен')
        break
    q_ind = input_list.find('Q')
    if q_ind != -1:
        input_list = input_list[0:q_ind]
        sum_of_numbers += sum_of_list(input_list)
        print('Вывод завершен')
        break
    sum_of_numbers += sum_of_list(input_list)
    print(sum_of_numbers)

print(sum_of_numbers)
