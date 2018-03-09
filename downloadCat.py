#!python3

#Download a Cat.py

import urllib.request as BB

res = BB.urlopen('http://placekitten.com/g/500/600')
##上面这一句等于下面两句
##i = BB.Request('http://placekitten.com/g/500/600')
##res = BB.urlopen(i)

cat_img = res.read()

with open('cat500x600.jpg','wb') as File:
    File.write(cat_img)
    
