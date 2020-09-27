# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = input('Введите целое положительное число: ')
max_num = 0

# while True:
#     try:
#         num_int = int(num)
#         if num_int > 0:
#             break
#         else:
#             num = input('Введено отрицательное значение или 0! Введите целое положительное число: ')
#     except:
#         num = input('Введено некоректное значение! Введите целое положительное число: ')
# for symbol in num:
#     current_num = int(symbol)
#     if current_num > max_num:
#         max_num = current_num

while True:
    if num.isdigit():
        break
    else:
        num = input('Введено некорректное значение! Введите целое положительное число: ')

num_int = int(num)
length = len(num)
exponent = int(10 ** (length-1))
i = 0

while i < length:
    i += 1
    current_num = num_int // exponent
    num_int = num_int % exponent
    if current_num > max_num:
         max_num = current_num
    exponent = int(10 ** (length-1-i))  # int(exponent / 10)
print(f'Самая большая цифра в числе - {max_num}')