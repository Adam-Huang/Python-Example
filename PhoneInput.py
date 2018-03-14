#! python3

import os
import time

def _fUnlock():
    os.system('adb shell input keyevent 26')
    time.sleep(1)
    os.system('adb shell input swipe 250 1000 250 500 500')
    time.sleep(1)

def _fBack():
    os.system('adb shell input keyevent 4')
    time.sleep(1)
    
def _fEnter():
    os.system('adb shell input tap 360 800')
    time.sleep(1)

def _fClear():
    time.sleep(2)
    os.system('adb shell input keyevent 3')##Home
    time.sleep(1)
    os.system('adb shell input keyevent 82')##菜单
    time.sleep(1)
    os.system('adb shell input tap 360 1150')##清除

def _fAutoRedbag():
    os.system('adb shell input tap 430 740')##支付宝
    time.sleep(10)
    os.system('adb shell input tap 209 1225')##财富
    time.sleep(0.5)
    _fEnter()
    time.sleep(10)
    _fEnter()
    os.system('adb shell input tap 127 1100')##领取
    time.sleep(0.5)
    os.system('adb shell input tap 600 930')##阅读吧
    time.sleep(5)
    _fBack()
    os.system('adb shell input tap 600 1100')##redbag
    time.sleep(1)
    _fEnter()
    time.sleep(10)
    _fEnter()
    _fBack()
    _fBack()
    _fEnter()
    os.system('adb shell input tap 308 1111')##浇花
    time.sleep(2)
    os.system('adb shell input tap 308 1111')##浇花
    _fClear()

def _fAutoPay():
    os.system('adb shell input tap 430 740')##支付宝
    time.sleep(10)
    os.system('adb shell input tap 500 1200')##friend
    time.sleep(1)
    os.system('adb shell input tap 550 600')##adadm
    time.sleep(1)
    os.system('adb shell input tap 170 1060')##adadm
    time.sleep(1)
    os.system('adb shell input swipe 550 600 550 600 1000')##长安
    time.sleep(1)
    os.system('adb shell input tap 470 780')##识别
    time.sleep(1)
    os.system('adb shell input tap 222 550')##金额
    time.sleep(1)
    os.system('adb shell input keyevent 9')##输入2
    time.sleep(1)
    os.system('adb shell input tap 400 790')##金额
    time.sleep(3)
    os.system('adb shell input tap 400 1200')##确认
    time.sleep(3)
    os.system('adb shell input tap 140 920')##1
    time.sleep(1)
    os.system('adb shell input tap 140 920')##
    time.sleep(1)
    os.system('adb shell input tap 600 1125')##
    time.sleep(1)
    os.system('adb shell input tap 600 1005')##
    time.sleep(1)
    os.system('adb shell input tap 360 1111')##
    time.sleep(1)
    os.system('adb shell input tap 600 1005')##
    time.sleep(1)
    _fClear()
