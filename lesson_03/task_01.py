# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def divide_result(numerator, denominator):
    if denominator == 0:
        return None
    return round(numerator / denominator, 2)


def is_num(num):
    try:
        float(num)
        return True
    except :
        return False


def input_number(question):
    number = input(question)
    while not is_num(number):
        number = input(f'Введено некорректное значение! {question}: ')
    else:
        return float(number)

# division_zero
num_1 = input_number('Ввести знаменатель: ')
num_2 = input_number('Ввести числитель: ')

result = divide_result(num_1, num_2)
if result is not None:
    print(f'{num_1} / {num_2} = {result}')
else:
    print('На 0 делить нельзя.')

