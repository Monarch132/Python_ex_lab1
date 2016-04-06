# -*- coding: utf-8 -*-
"""
Написать программу, которая позволяет ввести с клавиатуры \
натуральное число N \
и вывести на экран все комбинации натуральных чисел x, y, z, \
таких что x3+y3+z3=N. \
Если число N невозможно разложить по кубам x, y, z,\
программа должна выводить сообщение «No such combinations!».\

"""

import math

N = int(raw_input("Введите натуральное число: "))
a = []
stN = int(N ** (1/3.0)) if N > 100 else N

for x in range(1, stN):
    for y in range(1, stN):
        for z in range(1, stN):
            if x**3 + y**3 + z**3 == N:
                a.append([x, y, z])

print a if not len(a) == 0 else "No such combinations!"
