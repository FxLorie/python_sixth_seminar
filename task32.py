# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

from random import randint

n = 10
list_1 = list()
for i in range(n):
    list_1.append(randint(-10,15))
print(list_1)

range_1 = [int(x) for x in input('Insert range: ').split()]
list_2 = list()
for i in range(len(list_1)):
    if list_1[i] in range(range_1[0],range_1[1]):
        list_2.append(i)
print(list_2)