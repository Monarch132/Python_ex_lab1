# -*- coding: utf-8 -*-
"""
Ввести с клавиатуры текст. \
Программно найти в нем и вывести отдельно все слова,\
которые начинаются с большого латинского символа (от A до Z)\
и заканчиваются 2 цифрами,\
например «Petr93», «Johnny70», «Service02».\
Использовать регулярные выражения. \

"""

import re

s = raw_input("Введите текст: ")

ns = re.findall(r'[A-Z]\w+[0-9]{2}\b', s)

print ns