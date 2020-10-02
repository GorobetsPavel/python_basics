# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.sort()
    return sum(my_list[-2:])


def get_num(num):
    try:
        num = float(num)
        return num
    except:
        return None


def input_number(question):
    number = input(question)
    while True:
        number = get_num(number)
        if number is None:
            number = input(f'Введено некорректное значение! {question}: ')
        else:
            break

    return number


num_1 = input_number('Введите 1 число: ')
num_2 = input_number('Введите 2 число: ')
num_3 = input_number('Введите 3 число: ')

max_2_numbers = my_func(num_1, num_2, num_3)
print(f'Сумма максимальных 2х чисел из введенных = {max_2_numbers}')
