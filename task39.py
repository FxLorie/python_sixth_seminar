# Задача №39. Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

from random import randint

n = 8
m = 5
list_1 = list()
list_2 = list()
for i in range(n):
    list_1.append(randint(1,10))
print(list_1)
for i in range(m):
    list_2.append(randint(1,10))
print(list_2)

list_3 = list()
for i in list_1:
    if i not in list_2:
        list_3.append(i)
print(list_3)