#!python3
#stopwatch.py - A simple stopwatch program

import time as t

input()
starttime = t.time()
print('Start Counting')
try:
    while True:
        input()
        endtime = t.time()
        print('It\'s gone ' + str(round((endtime - starttime),4)))
        print('Entre \'Ctrl + C\' Can stop counting')
except KeyboardInterrupt:
    print('Bye-Bye!')
