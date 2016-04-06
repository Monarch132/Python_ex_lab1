# -*- coding: utf-8 -*-
"""
Модифицировать код задания 11: вывести все N от 1 до 100000\
(и соответствующие им комбинации),\
которые раскладываются минимум по 3 разным суммам кубов.\

"""

import math

i = 100001

a = []
n = {}

for N in range(1, i):
    stN = int(N ** (1 / 3.0)) if N > 99 else N

    for x in range(1, stN):
        for y in range(1, stN):
            for z in range(1, stN):
                if x**3 + y**3 + z**3 == N:
                    if N in n:
                        n[N] += [[x, y, z]]
                    else:
                        n[N] = [[x, y, z]]

if not len(n) == 0:
    nn = [str(el) + ": " + str(n[el]) for el in n if len(n[el]) >= 3]
    for el in nn:
        print el
else:
    print "No such combinations!"
