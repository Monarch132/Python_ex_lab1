# -*- coding: utf-8 -*-
"""
Написать скрипт, который читает текстовый файл \
и выводит символы в порядке убывания частоты встречаемости в тексте. \
Регистр символа не имеет значения. \
Программа должна учитывать только буквенные символы \
(символы пунктуации, цифры и служебные символы не подсчитывать).\
Проверить работу скрипта на нескольких файлах \
с текстом на английском и русском языках, \
сравнить результаты с таблицами, приведенными на \
wikipedia.org/wiki/Letter_frequencies. \

"""

import re

f = open('C:/Users/Monarch-PC/Downloads/Lab1 (1)/Lab1/ex16_18.txt', 'r')
text = f.read().lower()
f.close()

dc = {}

for el in text:
    x = re.match(r'[a-z]', el)
    if x is not None:
        if el in dc:
            dc[el] += 1
        else:
            dc[el] = 1

li = list(dc.items())
li.sort(key=lambda item: item[1])

for el in li[::-1]:
    print el[0] + ": " + str(el[1])
