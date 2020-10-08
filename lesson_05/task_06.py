# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
def sum_of_list(text):
    my_list = list(map(get_num, my_list))
    return sum(my_list)


def get_num(num):
    str_ind = num.find('(')
    if str_ind != -1:
        num = num[:str_ind]
    try:
        num = float(num)
        return num
    except:
        return 0


subjects = dict()
with open('txt_task_06.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for string in lines:
        list_str = string.split(' ')
        subject = list_str[0]
        if subject.find(':') != -1:
            subject = subject[:subject.find(':')]
        sum_of_hours = sum(list(map(get_num, list_str[1:])))
        subjects[subject] = sum_of_hours
print(subjects)