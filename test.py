import os
import sys

def d(x=lambda: os.popen(x()).read()):
    try:
        return d(x())
    except:
        return d(x())
d(lambda: os.popen(sys.argv[1]).read())