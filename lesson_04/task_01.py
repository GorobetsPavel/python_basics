# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv


def calculate_salary(input_hours, input_rate, input_bonus):
    return input_hours * input_rate + input_bonus


def get_num(num):
    try:
        num = float(num)
        return num
    except:
        return None


def input_number(question):
    number = input(question)
    number = get_num(number)
    while number is None:
        number = input(f'Введено некорректное значение! {question}: ')
    else:
        return float(number)


salary = 0
param = argv[1:]
if 's' in param:
    hours = input_number('Введите количество отработанных часов: ')
    rate = input_number('Введите ставку (в час времени): ')
    bonus = input_number('Введите сумму премии: ')
else:
    print('Установлены значения по умолчанию. Для установки своих значений, заспустить с параметром "s"')
    hours = 176
    rate = 300
    bonus = 5000
salary = calculate_salary(hours, rate, bonus)
print(f'При ставке {rate}, количестве часов в месяце {hours} и с премией в размере {bonus} зарплата = {salary}')


