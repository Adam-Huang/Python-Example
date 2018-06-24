##自动截取百度地图脚本
##默认截图大小1750x710, 截图张数100(10x10)张
##

import pyautogui as Au
import time

startpos = (0,190)
endpos =(1750,900)
jietupos = (772, 47)

def main():
    print('请先打开百度地图，然后让其全屏显示')
    print('截图张数100张，分布10x10,每张图片大小为：1750x710')
    print('请确认设置<截图工具>的快捷方式为Ctrl + Alt + ;')
    
    Au.click(startpos)
    y = 0
    while y < 5:
        x = 0
        while x < 5:
            Au.hotkey('ctrl','altleft',';')
            time.sleep(2)
            Au.click(jietupos)
            time.sleep(2)
            Au.moveTo(startpos,duration=2)
            time.sleep(2)
            Au.dragTo(endpos,duration=2.0)
            time.sleep(4)
            Au.hotkey('ctrl','s')
            time.sleep(2)
            strtemp = 'Line-' + str(y) + 'Colunms-' + str(x)
            Au.typewrite(strtemp)
            time.sleep(2)
            Au.typewrite('\n')
            time.sleep(2)
            Au.hotkey('altleft','f4')
            time.sleep(2)
            Au.moveTo(endpos,duration=2)
            Au.click(Au.position())
            time.sleep(2)
            Au.dragRel(-1750,0,duration=20)
            x+=1
            time.sleep(2)
        x = 0
        while x < 6:
            Au.moveTo(startpos,duration=2)
            time.sleep(2)
            Au.dragRel(1750,0,duration=2)
            Au.click(Au.position())
            time.sleep(2)
            x+=1
        Au.moveTo(endpos,duration=2)
        Au.dragRel(0,-710,duration=2)
        Au.click(Au.position())
        time.sleep(2)
        y+=1
    


if __name__ == '__main__':
    main()
