#!python3

##这个函数用来将指定手机的初始坐标输入进去，然后写到文件里以备读出的
import random

def RecordData(*position):
    if len(position) != 6:
        print('请输入4个数字，分别代表第一个图标的左上角值和右下角值，以及x方向和y方向的增量值：\n')
        return
    fri_x,fri_y,fri_ex,fri_ey,add_x,add_y = position
    file = open('PhonePosition.txt','w')
    index = 0
    for i in range(5):
        for j in range(4):
            index = index + 1
            xx = fri_x + add_x * j
            xe = fri_ex + add_x * j
            file.write(str(index) + ':' + str(xx) +',' + str(fri_y) +',' + str(xe) +',' + str(fri_ey) + '\n')
        fri_y = fri_y + add_y
        fri_ey = fri_ey + add_y
    file.close()


def GetInPosition(index):
    try:
        file = open('PhonePosition.txt')
    except:
        return (0,0,0,0)
    for each_line in file:
        position = file.readline()
        if int(position.split(':')[0]) == index:
            position1 = position.split(':')[1]
            break
    position = position1.split(',')
    return random.randint(int(position[0]),int(position[2])),random.randint(int(position[1]),int(position[3]))
        
