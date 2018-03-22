import urllib.request as URL

url = 'http://www.whatismyip.com.tw'

proxy01 = URL.ProxyHandler({'http':'45.78.28.141:625'})

opener01 = URL.build_opener(proxy01)

URL.install_opener(opener01)

res = URL.urlopen(url)

