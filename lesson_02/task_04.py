# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

sentence = input('Введите предложение: ')

split_sentence = sentence.split(' ')
print(split_sentence)

for index, word in enumerate(split_sentence, start=1):
    print(f'{index}. {word[0:10]}')
