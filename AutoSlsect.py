#!python3
#自动查找并打开网页脚本
#输入关键字，自动用默认浏览器打开网页

import webbrowser as WEB
import requests as R
import sys

if len(sys.argv) < 2:
    print('至少要两个参数\n')
    return
param = sys.argv[1:]
res = R.get('https://www.baidu.com/s?wd=' + param)
res.raise_for_status()

