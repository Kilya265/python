# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input())
y = int(input())
if x == 0 and y == 0:
    print('Координаты нулевые')
elif x > 0:
    print('1') if y > 0 else print('4')
else:
    print('2') if y > 0 else print('3')
