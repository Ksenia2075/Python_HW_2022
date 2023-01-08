# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
# out
# [4, 2, 4, 9]
#8

from random import randrange

# функция принимает число n и выдает список чисел количество которых равно n
def get_list (n: int) -> list:
    res_list = []
    for i in range(1, n + 1):
        j = randrange(100)
        res_list.append(j)
    return res_list

# функция принимает список ии выдает сумму элементов на нечетных позициях (не индексах)
def sum_odd_elem (list_a: list) -> int:
    sum = 0
    for i in range(0, len(list), 2):
        sum = sum + list[i]
    return sum


num = int(input('Введите число: '))
list_a = get_list(num)

print(list_a)
print(sum_odd_elem(list_a))


