#!python3
##应该是小甲鱼上翻译的例子

import urllib.request as URL
import urllib.parse as URP
import sys,pyperclip


url = 'http://fanyi.baidu.com/langdetect'

data = {}
head = {}
data['query'] = 'baby'
#data['from'] = 'AUTO'
#data['to'] = 'AUTO'
#data['smartresult'] = 'dict'
#data['client'] = 'fanyideskweb'
#data['salt'] = '1521110226055'
#data['sign'] = '8910adef2e64da0b7a9a10663db80219'
#data['doctype'] = 'json'
#data['version'] = '2.1'
#data['keyfrom'] = 'fanyi.web'
#data['action'] = 'FY_BY_CLICKBUTTION'
#data['typoResult'] = 'false'
'''
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
'''

data = URP.urlencode(data).encode('utf-8')
req = URL.Request(url,data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
res = URL.urlopen(req)
res.status
html = res.read().decode('utf-8')
print(html)
html = res
