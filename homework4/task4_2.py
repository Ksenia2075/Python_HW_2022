# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн
# in 54
# out [2, 3, 3, 3]
# in 9990
# out [2, 3, 3, 3, 5, 37]
# in 650
# out [2, 5, 5, 13]


# функция возвращает список чисел, которые являются простыми множителями введенного числа
def simple_multiplier (num: int) -> list:
    i = 2 # первое простое число
    list = []
    while i <= num:
        if num % i == 0:
            list.append(i)
            num //= i
            i = 2
        else:
            i += 1
    return list

num = int(input("Введите число: "))
print(simple_multiplier(num))


