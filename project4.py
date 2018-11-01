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