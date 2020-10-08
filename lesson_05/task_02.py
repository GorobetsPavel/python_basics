# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('txt_task_02.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f'Всего строк {len(lines)}')
    for i, string in enumerate(lines, 1):
        words = string.split(' ')
        print(f'В строке №{i} содержится {len(words)} слов')








