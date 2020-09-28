# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
from random import randint

length = randint(3, 9)
my_list = []

for i in range(length):
    my_list.append(randint(0, 9))

print(my_list)

i = 1
while i < length:
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
    i += 2

print(my_list)