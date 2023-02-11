# -*- coding: utf-8 -*-

# -- Sheet --

from sympy import *
from sympy.plotting import plot

x = Symbol("x")
f = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
f 

solveset(f, x, Reals).evalf(2)

items = [-oo, oo]
items[1:1] = solveset(diff(f), x, Reals).evalf(2)
items.sort()
items

up = []
down = []
for i in range(1, len(items)):
    move = is_increasing(f, Interval.open(items[i-1], items[i]))
    if move:
        up.append(f'{items[i-1], items[i]}')
    else:
        down.append(f'{items[i-1], items[i]}')
print('Вщзрастает в интервале', *up)
print('Убывает в интервале', *down)

plot(f, (x, -100, 100))

from random import uniform
items = sorted(solveset(diff(f), x, Reals).evalf(2))
items.insert(0, items[0] -1)
f_diff = diff(f)
ls = []
for i, val in enumerate(items):
    ls.append(f_diff.subs(x, uniform(val, items[i] + 1)))
    if i != 0:
        if ls[i-1] < 0 < ls[i]:
            print('Точка минимума', val, f.subs(x, val).evalf(2))
        elif ls[i-1] > 0 > ls[i]:
            print('Точка максимума', val, f.subs(x, val).evalf(2))

solveset(f > 0, x, Reals).evalf(2) 

solveset(f < 0, x, Reals).evalf(2)



