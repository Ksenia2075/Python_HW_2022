# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции
# преобразования, без строк.
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011

# функция принимает десятичное число и выдает двоичное
def int_to_binary (n: int) -> str:
    result = ''
    while n > 0:
        result = str(n % 2) +result
        n = n // 2
    print(result)

int_to_binary(int(input('Введите чиисло: ')))


# Вариант с урока
# def conv_bin (num: int):
#     list_nums = []
#     while num > 0:
#         list_nums.insert(0, num % 2)
#         num //= 2
#     print(*list_nums, sep="")
#
# conv_bin(int(input('Введите чиисло: ')))



