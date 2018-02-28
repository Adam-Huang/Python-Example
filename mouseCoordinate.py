#！ python3

import pyautogui as G

print('Please entre the \'ctrl + C\' to stop!')

try:
    while True:
        x,y = G.position()
        str1 = str(x) + ',' + str(y)
        print(str1,end = '')
        print('\b'*len(str1),end = '',flush = True)
except KeyboardInterrupt:
    print('Bye-Bye!')
