import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

curkey = None
maxi = -100000
mini = 100000


for line in sys.stdin:

    key, val = line.split(",")
    val = float(val)

    if key == curkey:

        if val < mini:
            mini = val 
        
        if val > maxi:
            maxi = val
    else:
        
        if curkey is not None:
            
            sys.stdout.write("{}\t{}\t{}\n".format(curkey, maxi, mini))

        curkey = key
        mini = val
        maxi = val

sys.stdout.write("{}\t{}\t{}\n".format(curkey, maxi, mini))