# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('txt_task_03.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for string in lines:
        data = string.split(' ')
        salary = float(data[1])
        if salary < 20000:
            print(string.strip())




