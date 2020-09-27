# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

def is_num(num):
    try:
        float(num)
        return True
    except:
        return False


proceeds = input('Введите значение выручки: ')
while not is_num(proceeds):
    proceeds = input('Введенное значение не является числом. Введите значение выручки: ')
else:
    proceeds = float(proceeds)

costs = input('Введите значение издержек: ')
while not is_num(costs):
    costs = input('Введенное значение не является числом. Введите значение издержек: ')
else:
    costs = float(costs)

profit = proceeds - costs
if profit > 0:
    print(f'Прибыль = {profit}')
    profitability = round(profit / proceeds * 100, 2)
    print(f'Рентабельность составила {profitability}%')

    employees = input('Введите количество сотрудников в фирме: ')
    while not employees.isdigit():
        employees = input(
            'Введенное значение не является целым, положительным числом. Введите количество сотрудников в фирме: ')
    else:
        employees = float(employees)

    profit_on_1 = round(profit / employees, 2)
    print(f'Прибыль на 1 сотрудника составляет {profit_on_1}')

elif profit < 0:
    print(f'Убыток = {-profit}')
else:
    print('Компания работает без прибыли')
