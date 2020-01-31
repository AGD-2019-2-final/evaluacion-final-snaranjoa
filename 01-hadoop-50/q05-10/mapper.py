import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.strip()
    line = line.split(' ')
    temp = line[3]
    temp = temp.split('-')
    temp = temp[1]
    sys.stdout.write("{},1\n".format(temp))