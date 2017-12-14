# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def extract_image(text):
    soup = BeautifulSoup(text, "lxml")
    elems = soup.find_all('img', {'class': "BDE_Image"})
    return [elem.get("src")
            for elem in elems if elem.get("src").find("forum") > -1]


if __name__ == "__main__":
    img_urls = extract_image(get_html("http://tieba.baidu.com/p/2166231880"))
    print('\n'.join(img_urls))
