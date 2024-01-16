import os
import sys

x = lambda: os.popen(str(sys.argv[1])).read()
x()