#Д/з 1 
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# n = int(input("введите цифру, обозначающую день недели: "))
# if n >= 1 and n <= 5:
#     print("не выходной")
# elif n >= 6 and n <= 7:
#      print("выходной")

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀ - and
# ⋁ - or
# ¬ - not

# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input("введите координату точки x: "))
# y = int(input("введите координату точки y: "))
# if x > 0 and y > 0:
#     print("1")
# elif x < 0 and y > 0:
#     print("2")
# elif x < 0 and y < 0:
#     print("3")
# elif x > 0 and y < 0:
#     print("4")

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input("введите номер четверти: "))
# if n == 1:
#     print("x > 0, y > 0")
# elif n == 2:
#     print("x < 0, y > 0")
# elif n == 3:
#     print("x < 0, y < 0")
# elif n == 4:
#     print("x > 0, y < 0")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# AХ = int(input("введите координату точки A оп оси Х: "))
# AY = int(input("введите координату точки A оп оси Y: "))
# BХ = int(input("введите координату точки B оп оси Х: "))
# BY = int(input("введите координату точки B оп оси Y: "))
# import math
# distans = math.sqrt((AХ-BХ)**2+(AY-BY)**2)
# #print('%.2f''Растояние между точкой A до точки B = {distans}')
# print('Растояние между точкой A до точки B: ' '%.2f' % distans)
