# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

# функция принимает число n и выдает список чисел от 0 до n - 1
def get_list (n):
    list = []
    x = 0
    list.append(x)
    for i in range(0, n - 1):
        x = x + 1
        list.append(x)
    return list

# функция принимает список чисел и перемешивает его не создавая новый
def mix_elements (list):
    n = len(list)
    for i in range(n):
        j = random.randint(0, n - 1)
        el = list.pop(j)
        list.append(el)
    return list


num = int(input('Введите число: '))
list_nums = get_list(num)

print(list_nums)
print(mix_elements(list_nums))


