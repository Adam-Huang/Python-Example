import time as t

starttime = t.time()
Sum = 1
for i in range(1,1000):
    Sum = Sum * i
endtime = t.time()
print('It\'s' + str(endtime - starttime))
print('result is '+ str(Sum))
