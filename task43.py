# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках

from random import randint

n = 8
list_1 = list()
for i in range(n):
    list_1.append(randint(1,10))
print(list_1)

set_1 = set(list_1)
count = 0

for i in set_1:
    count_1 = 0
    for j in list_1:
        if i == j:
            count_1 += 1
    if count_1 % 2 != 0:
        count_1 -= 1
    count += count_1//2
print(count)