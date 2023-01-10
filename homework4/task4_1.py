# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal

# функция выводит число с заданной точностью
def num_accuracy(n, a):

    print("Число с заданной точностью: ", n.quantize(a))


number = Decimal(input("Введите число: "))
accuracy= Decimal(input("Введите требуемую точность '0.0001': "))

num_accuracy (number, accuracy)


