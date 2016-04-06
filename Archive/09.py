# -*- coding: utf-8 -*-
"""
Сгенерировать случайным образом число N от 1 до 1000. \
Создать массив из N целых чисел,\
также сгенерированных случайным образом.\
Дополнить массив нулями до длины, равной ближайшей степени двойки. \
Например, если в массиве было N = 100 элементов,\
то дополнить массив 28 нулями, чтобы в итоге был массив из 28=128 элементов\
(ближайшая степень двойки к 100 – это число 128, для 73 – это 64 и т.д.).\

"""

import random

N = random.randint(1, 1000)
print "N = " + str(N)

a = [random.randint(1, 1000) for el in range(N)]

t = [2**el for el in range(11)]

for i in range(len(t)):
    if t[i] == N:
        break
    elif t[i] < N < t[i+1]:
        x = N - t[i]
        y = t[i+1] - N

        if x == y or x < y:
            while(len(a) > x):
                del a[-1]
        elif x > y:
            a.extend([0 for i in range(y)])
    i += 1
print a
print "a lenght = " + str(len(a))
