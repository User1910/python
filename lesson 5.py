print('задание 1')
print()
from itertools import groupby
l = ['a', 'a', 'a', 'f', 'h', 'k', 'k']
new_l = [el for el, _ in groupby(l)]
print(new_l)
print()

print("Задание 2")
print()
print('вариант 1')
n = 2
l1 = ['a', 'a', 'a', 'f', 'h', 'k', 'k']
l2 = l1 * n
print(l2)
print()
print("вариант 2")
a = [1, 7, 9]
b = a.copy()
print(b)
print()

print('Задание 3')
print()
list_1 = [5, 10, 15, 20, 25, 30]
list_2 = [10, 20, 30, 40, 50, 60]

list_difference = []
for element in list_1:
    if element not in list_2:
        list_difference.append(element)

print(list_difference)
print()

print('Задание 4')
print()
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
print()

print('Задание 5')
print()
d = dict()
for x in range(1, 16):
    d[x] = x**2
print(d)
print()