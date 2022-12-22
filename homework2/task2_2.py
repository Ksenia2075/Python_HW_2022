# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел
# от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

def multiply_num (num):
    list = []
    count = 1
    for i in range(1, num + 1):
        count *= i
        list.append(count)
    return list


number = int(input('Введите число: '))
print(multiply_num(number))



