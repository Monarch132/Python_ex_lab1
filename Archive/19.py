# -*- coding: utf-8 -*-
"""
Написать скрипт reorganize.py, \
который в директории --source \
создает две директории: Archive и Small.\
В первую директорию помещаются файлы с датой изменения,\
отличающейся от текущей даты на количество дней более --days.\
Во вторую – все файлы размером меньше параметра --size.\
Каждая директория должна создаваться только в случае,\
если найден хотя бы один файл,\
который должен быть в нее помещен.

Пример вызова:
    `reorganize --source "C:\TestDir" --days 2 --size 4096`

"""
import shutil
import os
import argparse
import sys
from time import time
from math import floor


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Script for organizing your folders')
    
    parser.add_argument('-s', '--source',
                        help='dir to work(abspath)',
                        default='')
    
    parser.add_argument('-d', '--days',
                        help='change date maximum',
                        default='1')
    
    parser.add_argument('-S', '--size',
                        help="maximum size of file (bytes)",
                        default='2048')
    
    res_args = parser.parse_args(args)
    
    return (res_args.source,
            res_args.days,
            res_args.size)


def reorganize(source, days, size):
    if source == '':
        pass
    elif source[0] == '/':
        os.chdir(source)
    else:
        os.chdir(os.path.join(os.getcwd(), source))

    archive = []
    small = []
    
    for root, dirs, files in os.walk(os.getcwd()):
        if root == os.getcwd():
            for f in files:
                if f == '.DS_Store':
                    continue
                
                secs = time() - os.path.getmtime(os.path.join(f))
                m_days = int(floor(secs / (60 * 60 * 24)))
                days = int(days)
                
                if m_days > days:
                    archive += [f]
                elif os.path.getsize(os.path.join(f)) < int(size):
                    small += [f]
    
    if not archive and not small:
        return 'Nothing to do'
    
    res = 'Archive:\n'
    if archive:
        res += do_movements(archive, 'Archive')
    res += 'Small:\n'
    if small:
        res += do_movements(small, 'Small')
        
    return res
    

def do_movements(files, type_):
    if not os.path.exists(os.path.join(os.getcwd(), type_)):
        os.mkdir(type_)
    result = ''
    for f in files:
        shutil.move(os.path.abspath(os.path.join(os.getcwd(), f)),
                    os.path.abspath(os.path.join(os.getcwd(), type_, f)))
        result += '- ' + f + '\n'
    return result


if __name__ == '__main__':
    """
    01, 02, 05, 10 : edited: today,
                     size > 2048

    04, 08         : edited: today,
                     size < 2048

    03, 06, 07, 09 : edited: !today,
                     size < 2048

    """
    s, d, S = parse_args(sys.argv[1:])
    print reorganize(s, d, S)