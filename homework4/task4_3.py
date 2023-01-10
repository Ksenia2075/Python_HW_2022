# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности в том же порядке.
# in 7
# out [4, 5, 3, 3, 4, 1, 2]
#     [5, 1, 2]
# in -1
# out Negative value of the number of numbers!
#     []
# in 10
# out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
#     [6, 2, 3, 0, 9]

from random import randint

# функция выдает список целых чисел, кол-во вводит пользователь
def get_num_list(num: int) -> list:
    num_list = []
    if num < 1:
        return "Вы ввели отрицательное значение количества чисел!"
    else:
        for i in range(num):
            num_list.append(randint(0, 9))
    return num_list

# функция принимает список, проверяет повторяются ли элементы и выдает список в том же порядке без повторения элементов
def find_uniq_num(list) -> list:
    temp = {}
    for i in list:
        if i in temp:
            temp[i] = False
        else:
            temp[i] = True

    output = [i for i in temp if temp[i]]
    return output


num = int(input("Введите длину списка: "))
list_a = get_num_list(num)
print(list_a)
print(find_uniq_num(list_a))


