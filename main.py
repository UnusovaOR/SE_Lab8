#Лабораторная работа 8, вариант 13, студент Юнусова Оксана Руслановна, группа 2023-ФГиИБ-ПИ-1см

from matplotlib import pyplot as plt

c = 0
q = 0
s = 0
with open('data.csv', 'r') as file:
    for line in file:
        lst = line.rstrip().split(',')
        if lst[1] == '0' and lst[6] != '' and float(lst[6]) < 18:
            if lst[12][:-1] == 'C':
                c = c + 1
            elif lst[12][:-1] == 'Q':
                q = q + 1
            elif lst[12][:-1] == 'S':
                s = s + 1
print(f'Шербур - {c}, Квинстаун - {q}, Саутгемптон - {s}')
embarked = ['Шербур', 'Квинстаун', 'Саутгемптон']
count = [c, q, s]
plt.bar(embarked, count)
plt.show()
