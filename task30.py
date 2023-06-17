# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# list_1 = list()
# list_1.append(int(input('First element: ')))
# diff = int(input('Difference between elements: '))
# number = int(input('Number of elements: '))
# for i in range(2, number):
#     list_1.append(list_1[0]+(i-1)*diff)
# print(*list_1)

## 2 вариант
list_1 = list()
first_element = int(input('First element: '))
diff = int(input('Difference between elements: '))
number = int(input('Number of elements: '))
for i in range(first_element, number*diff+first_element, diff):
    list_1.append(i)
print(*list_1)