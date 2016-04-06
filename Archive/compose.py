"""
# FILE COMPOSER

COMPOSE ALL FILES WITH NUMERIC NAME:
* FROM i,5, 10

* TO maxi
* IN DIRECTORY path
* TO FILE all.txt

> NOTE: YOU CAN ALSO USE CONSOLE ARGS
    
FOR EXAMPLE: 
`bash#: python /PathToCompose/compose.py 1 20 "/Users/My/Python/Files/"`

"""
import sys
import os

def __file_composer__(i, maxi, path):
    res_path = os.path.join(path, 'all.txt')
    print res_path
    open(res_path, 'w').close()

    for file_ in range(i, maxi + 1):

        if i < 10:
            file_ = open(os.path.join(path, '0' + str(i) + '.py'), 'r')
        else:
            file_ = open(os.path.join(path, str(i) + '.py'), 'r')

        text = file_.read()
        file_.close()

        file_ = open(res_path, 'a')
        file_.write(text + "\n\n")
        file_.close

        print str(i) + '.py ready.' + '\n'

        i+=1

    return True

if __name__ == "__main__":
    sa = sys.argv

    if len(sa) > 1 < 5:
        i, maxi, path = sa[1], sa[2], sa[3]
    else:
        i, maxi, path = raw_input('Input i, maxi, path: ').split(',')

fc = __file_composer__(int(i), int(maxi), str(path))

print 'all ready.' if fc else 'something bad :('