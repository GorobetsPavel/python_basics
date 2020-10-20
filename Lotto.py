from random import randint, shuffle
import numpy


class Card:
    def __init__(self, name):
        self.card = self.generate_card()
        self.name = name
        self.count = 15

    def __sub__(self, other):
        length = len(other)
        self.card = self.card.replace(other, ' ' * (length - 2) + '- ')
        self.count -= 1

    @staticmethod
    def generate_card():
        all_nums = [i for i in range(1, 91)]
        card = ''
        for row in range(0, 3):
            # my_list = ['□' for el in range(4)]
            my_list = ['' for el in range(4)]
            for i in range(0, 5):
                my_list.append(str(all_nums.pop(randint(0, len(all_nums) - 1))))
            shuffle(my_list)
            # card += ''.join(str(i) for i in my_list) + '\n'
            card += ' '.join((3 - len(i)) * ' ' + i + ' ' for i in my_list) + '\n '
        return card


player_card = Card('Карточка игрока')
comp_card = Card('Карточка компьютера')

nums_for_game = [i for i in range(1, 91)]

while True:
    num = str(nums_for_game.pop(randint(0, len(nums_for_game) - 1)))
    print(comp_card.name + '\n', comp_card.card)
    print(player_card.name + '\n', player_card.card)
    print(f'\nНовый бочонок: {num} (осталось {len(nums_for_game)})')

    num = ' ' + num + ' '
    # print(player_card.card.find(num))

    answer = input('Зачеркнуть цифру? (y/n)')
    answer = answer.lower()

    find_num = player_card.card.find(num)

    if answer == 'y':
        if find_num == -1:
            print('Такого числа нет на вашей карточке, вы проиграли! Игра завершена')
            break
        else:
            player_card - num

        if comp_card.card.find(num) != -1:
            comp_card - num

        if player_card.count == 0:
            print('Вы выиграли!')
            break
        elif comp_card.count == 0:
            print('Компьютер выиграл!')
            break
    elif answer == 'n':
        if find_num != -1:
            print('Такое число есть на вашей карточкеб вы проиграли! Игра завершена')
            break

        if comp_card.card.find(num) != -1:
            comp_card - num
            if comp_card.count == 0:
                print('Компьютер Выиграл!')
                break
    else:
        print('\n Некорректный ответ! Игра завершена!')
        break
