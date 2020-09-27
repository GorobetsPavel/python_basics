# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = input('Введите число: ')
sum = 0
example = ''

while True:
    try:
        num_int = int(num)
        break
    except:
        num = input('Введено некоректное значение! Введите число: ')

i = 1

while i <= 3:
    current_num = num * i
    if example != '':
        example += ' + ' + current_num
    else:
        example = current_num

    num_int = int(current_num)
    sum += num_int
    i += 1

print(example, ' = ', sum)


