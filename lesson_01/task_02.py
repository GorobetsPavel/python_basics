# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_sec = input('Введите время в секундах: ')

while True:
    try:
        time_in_sec = int(time_in_sec)
        break
    except:
        time_in_sec = input('Введено некоректное значение! Введите время в секундах (число): ')

hours = time_in_sec // 3600
minutes = time_in_sec % 3600 // 60
seconds = time_in_sec % 60

print(f'{hours}:{minutes}:{seconds}')
