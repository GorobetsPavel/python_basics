# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

profitable_firms = {}
unprofitable_firms = {}
all_profit = 0
# loss = 0
with open('txt_task_07.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for string in lines:
        list_str = string.split(' ')
        firm = list_str[0]
        profit = float(list_str[2]) - float(list_str[3])
        if profit >= 0:
            profitable_firms[firm] = profit
            all_profit += profit
        else:
            unprofitable_firms[firm] = profit
            # loss += profit

list_with_profit = [profitable_firms, {'average_profit': all_profit / len(profitable_firms.keys())}]
# list_with_loss = [profitable_firms, {'average_loss': loss / len(unprofitable_firms.keys())}]

# print(profitable_firms)
# print(unprofitable_firms)
with open('txt_task_07.json', 'w', encoding='utf-8') as file:
    json.dump(list_with_profit, file)