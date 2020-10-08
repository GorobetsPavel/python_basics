# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

new_text = ''
with open('txt_task_04.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for string in lines:
        if string.find('One') >= 0:
            new_text += string.replace('One', 'Один')
        elif string.find('Two') >= 0:
            new_text += string.replace('Two', 'Два')
        elif string.find('Three') >= 0:
            new_text += string.replace('Three', 'Три')
        elif string.find('Four') >= 0:
            new_text += string.replace('Four', 'Четыре')

with open('txt_task_04_2.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)