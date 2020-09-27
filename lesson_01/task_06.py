# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

def is_positive_num(num):
    try:
        num = float(num)
        if num > 0:
            return True
        else:
            return False
    except:
        return False


progress = 1.1
day = 1

result = input('Введите результат первого дня: ')
while not is_positive_num(result):
    result = input('Введенное значение не является положительным числом. Введите корректный результат первого дня: ')
else:
    result = float(result)

required_result = input('Введите результат, который вы хотите достичь: ')
while not is_positive_num(required_result):
    required_result = input('Введенное значение не является положительным числом. Введите корректный результат первого дня: ')
else:
    required_result = float(required_result)

while result < required_result:
    result = result * progress
    day += 1
else:
    print(f'на {day}-й день спортсмен достигнет результата — не менее {required_result}')