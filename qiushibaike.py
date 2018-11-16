# -*- coding:utf-8 -*-
import requests
import re
import time
import threading

tc = 5
tl = []
page = input('input page:\n')
req = requests.get('https://www.qiushibaike.com/imgrank/page/%s' % page)
imglist = re.findall(r'pic.*medium.*\.jpg', req.text)


def dlimg(url):
    global tc
    tc -= 1
    h = 'http://%s' % url
    print(h)
    p = requests.get(h)
    with open(h.split('/')[-1], 'wb') as f:
        f.write(p.content)
    tc += 1


for i in imglist:
    tl.append(threading.Thread(target=dlimg, args=[i]))

for i in tl:
    while not tc:
        time.sleep(1)
    i.start()
