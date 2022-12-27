# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randrange

# функция принимает число n и выдает список чисел количество которых равно n
def get_list (n: int) -> list:
    list = []
    for i in range(1, n + 1):
        j = randrange(10)
        list.append(j)
    return list

# функция принимает список и выдает результирующий список произведений пар чисел из списка
# где парой считаем первый и последний элемент
def multiply_elem (list) -> list:
    res_list = []
    len_list = len(list)
    for i in range(len_list // 2):
        res_list.append(list[i] * list[len_list - i - 1])
    if len_list % 2:                                        # если нечетное кол-во элементов то добавляем элемент
        res_list.append(list[len_list // 2])            #  с индексом (целая часть от деления длинны списка на 2)
    return res_list


num = int(input('Введите число: '))
list_a = get_list(num)
print(list_a)
print(multiply_elem(list_a))




