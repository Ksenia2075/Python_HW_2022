# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
#
# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

# функция принимает число и выдает список от -n до n
def fill_list (n):
    list = []
    f = -n
    list.append(f)
    for i in range(-n, n):
        f = f + 1
        list.append(f)
    return list

# функция принимает список, число а и число в, выдает произведение элементов на позициях а и в
def multiply_position (list, a, b):
    if a < len(list) and b < len(list):
        return (list[a - 1] * list[b - 1])
    else:
        return 'Этих позиций нет'


numN = int(input('Введите число N: '))
numA = int(input('Введите первую позицию: '))
numB = int(input('Введите вторую позицию: '))

list_nums = fill_list(numN)
print(list_nums)
print(multiply_position(list_nums, numA, numB))