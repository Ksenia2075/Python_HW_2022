# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
#
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
#
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

# функция принимает число и выдает список чисел Фибоначи начиная с отрицательных индексов
def negafibonacci (n: int):
    fibo = [1, 1]
    negafibo = [1, -1]

    for i in range(2, n):
        list = fibo[i - 1] + fibo[i - 2]
        fibo.append(list)
        list2 = negafibo[i - 2] - negafibo[i - 1]
        negafibo.append(list2)
    negafibo.reverse()
    fibo.insert(0, 0)
    print(*negafibo,*fibo, sep=' ')


num = int(input('Введите число: '))
negafibonacci(num)

#  Вариант с урока
def neg_fib(num: int):
    a, b = 1, 1
    list = [0]
    for i in range(num):
        list.append(a)
        list.insert(0, a * (-1) ** i)
        a, b = b, b + a
    return list

print(*neg_fib(int(input('Введите число: '))))



