# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

import random

# функция принимает число и выдает список из разных вариантов "абв" (кол-во заданно числом)
def rand_list_abv(count: int) -> list:
    txt = "абв"
    list = []
    if count <= 0:
        print("Ошибка! Вы ввели отрицательное число.")

    for x in range(count):
        random_txt = random.sample(txt, 3)  # k = 3
        list.append("".join(random_txt))
    return (' '.join(list))


# функция принимает список и исключает заданное значение
def new_list(list) -> list:
    ex = "абв"
    list2 = [item for item in list.split() if ex not in item]
    print(" ".join(list2))


result = rand_list_abv(int(input("Введите длину списка: ")))
print(result)
print()
print("Список без слов 'абв': ")
print(new_list(result))


