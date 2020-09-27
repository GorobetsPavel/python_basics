# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
def get_number_of_month(num) -> object:
    if num.isdigit():
        month = int(num)
        if 0 < month <= 12:
            return month
        else:
            return 0
    else:
        return 0


months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
          'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
seasons = ('Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима')

seasons_dic = dict()

for i in range(12):
    seasons_dic[i+1] = {'Season': seasons[i], 'Month': months[i]}

num_month = input('Введите номер месяца: ')
while True:
    num_month = get_number_of_month(num_month)
    if num_month != 0:
        break
    else:
        num_month = input('Введено некорректное значение. Необходимо ввести номер месяца (от 1 до 12): ')

# print(f'Выбранный месяц - {months[num_month-1]}. Это {seasons[num_month-1]}')
input_month = seasons_dic.get(num_month)
month_name = input_month.get('Month')
month_season = input_month.get('Season')
print(f'Выбранный месяц - {month_name}. Это {month_season}')


