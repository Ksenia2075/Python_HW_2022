# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform


# функция принимает число n и выдает список вещественных чисел количество которых равно n
def get_float_list (n: int) -> list:
    res_list = []
    for i in range(1, n + 1):
        j = uniform(0, n)
        res_list.append(round(j, 2))
    return res_list

# функция принимает список вечественных чисел и выдает максимальное значение дробной части,
# минимальное значение дробной части и разницу между ними
def minmax (list):
    max_min = []
    for i in range(len(list)):
        if list[i]%1 != 0:
            max_min.append(list[i]%1)
            dif = round(max(max_min) - min(max_min), 2)
    return f"Max: {round(max(max_min), 2)}, Min: {round(min(max_min), 2)}, Difference: {dif}"



num = int(input('Введите число: '))
list_a = get_float_list(num)

print(list_a)
print(minmax(list_a))


# Вариант с урока
def dif_max_min(list):
    num_max = num_min = list[0] % 1

    for i in range(1, len(list)):
        num = round(list[i] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f"Min: {num_min:.2f}, Max: {num_max:.2f}, Difference: {result}")
    return result

print(dif_max_min(list_a))



