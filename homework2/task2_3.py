# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

# функция принимает число и выдает список заполненный по формуле
def some_list (number):
    list = []
    for i in range (1, number + 1):
        list.append(round(((1 + 1 / i) ** i), 3))
    return list

# функция принимает список и выдает сумму элементов списка
def sum_list (list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum


num = int(input('Введите число: '))
num_list = some_list(num)
print(num_list)
print(sum_list(num_list))


