import urllib.request as URL
import os

def url_ope(url):
    req = URL.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')
    res = URL.urlopen(req)
    html = res.read()
    return html

def getpage(url):
    html = url_ope(url)
    html = html.decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']',a)

    return html[a:b]
    

def getimage(url):
    html = url_ope(url).decode('utf-8')
    img = []
    a = html.find('img src=')
    b = html.find('jpg',a,a+255)
    
    pass

def saveimage(url):
    pass

def download(folder = 'OOXX', page = 10):
    try:
        os.mkdir(folder)
    except:
        print('存在!')
    os.chdir(folder)

    url = 'http://jandan.net/ooxx'

    page_num = int(getpage(url))

    for i in range(page):
        page_num -= 1
        page_url = url + '/page-' + str(page_num) + '#comments'
        image_arr = getimage(page_url)
        saveimage(folder,image_arr)


if __name__ == '__main__':
    download()
