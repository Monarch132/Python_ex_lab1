# -*- coding: utf-8 -*-
"""
Написать скрипт, который выводит на экран TRUE, \
если элементы массива представляют собой возрастающую последовательность,\
иначе – FALSE. \

"""

a = [int(el) for el in raw_input('Введите массив: ').split()]
print 'TRUE' if a == sorted(a) else 'FALSE'
# one more thx to @BumagniyPacket
