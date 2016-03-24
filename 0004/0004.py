#!/usr/bin/env python

from collections import Counter
import re

def creat_list(filename):
    datalist = []
    with open(filename,'r') as f:
        for line in f:
             content = re.sub("\"|,|\.","",line)
             datalist.extend(content.strip().split(' '))
    return datalist

def wc(filename):
    print Counter(creat_list(filename))

if __name__ == "__main__":
    filename =  'test.txt'
    wc(filename)
