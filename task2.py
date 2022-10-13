# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

b = [False, True]
for x in b:
    for y in b:
        for z in b:
            left = not (x or y or z)
            right = not x and not y and not z
            print('Истина') if left == right else print('Ложь')
