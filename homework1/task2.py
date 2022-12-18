# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.
# (W and Z) or not Y or (not X == not W)

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not ((y and x) or (z and not x) or (not w and not x) or not y):
                    print(x, y, z, w)



