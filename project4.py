# coding=utf-8

import random

print('Загадано четырехбуквенное слово из букв А, E, Н, О, С, Т.')
print('Отгадай!')

letters = ['А', 'Е', 'Н', 'О', 'С', 'Т']
a = []
word = None
smn_place = None

for i in range(4):
    a.append(random.choice(letters))
counter = 1
while smn_place != 0:
    print('Попытка № {}: '.format(counter), end='')
    word = input()
    its_place = 0
    smn_place = 0
    for i in range(4):
        if a[i] == word[i]:
            its_place += 1
        else:
            smn_place += 1
    print('На "своем месте":', its_place)
    print('На "чужом месте":', smn_place)
    counter += 1
    if smn_place == 0:
        print('Вы выиграли!')
        print('Хочешь сыграть еще раз?:) ДА или НЕТ?')
        answer = input()
        if answer.upper() == 'ДА':
            smn_place = None
            counter = 1
        else:
            print('Тогда хорошего дня, приходи играть еще!')
            break