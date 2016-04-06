# -*- coding: utf-8 -*-
"""
Написать скрипт, позволяющий искать в заданной директории \
и в ее подпапках файлы-дупликаты\
на основе сравнения контрольных сумм (MD5).\
Файлы могут иметь одинаковое содержимое, \
но отличаться именами. \
Скрипт должен вывести группы имен обнаруженных файлов-дупликатов.\
Ниже приведен фрагмент кода для вычисления контрольной суммы:

    import hashlib
    ...
    f = open('file.txt', 'r' )
    data = f.read()
    f.close()
    checksum = hashlib.md5(data).hexdigest()

"""

import os
import re
import hashlib as hl


def walk(dir_path, files_dict):
    for el in os.listdir(dir_path):
        path = os.path.join(dir_path, el)

        if os.path.isfile(path):
            f = open(path, 'r')
            text = f.read()
            f.close()
            checksum = hl.md5(text).hexdigest()

            if checksum in files_dict:
                files_dict[checksum] += [path]
            else:
                files_dict[checksum] = [path]
        else:
            walk(path, files_dict)

os.chdir('/Users/prvz/Desktop/UNIVERSITY/Python/Lab1/ex17/')

path = os.getcwd()
files = {}

walk(path, files)

for el in files:
    print "\n" + el + ": " + str(files[el])
