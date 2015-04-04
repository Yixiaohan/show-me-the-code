#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
import re
import urllib.request

def get_html(url):
    return urllib.request.urlopen(url).read().decode('utf-8')

def get_image(html):
    reg = r'img pic_type="0" class="BDE_Image" src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    for index, imgurl in enumerate(imglist):
        urllib.request.urlretrieve(imgurl, '%d.jpg' % index)

if __name__ == '__main__':
    html = get_html("http://tieba.baidu.com/p/2166231880?fr_bdps_bottom_login=1")
    get_image(html)
