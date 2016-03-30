#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数

from collections import Counter
import re


def creat_list(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            content = re.sub("\"|,|\.", "", line)
            datalist.extend(content.strip().split(' '))
    return datalist


def wc(filename):
    print Counter(creat_list(filename))

if __name__ == "__main__":
    filename = 'test.txt'
    wc(filename)
