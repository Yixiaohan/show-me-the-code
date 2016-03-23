#!/usr/bin/env python

import glob
from collections import Counter
import re

def list_txt():
    return glob.glob("*.txt")

def wc(filename):
    datalist = []
    with open(filename,'r') as f:
        for line in f:
             content = re.sub("\"|,|\.","",line)
             datalist.extend(content.strip().split(' '))
    #print datalist
    return Counter(datalist).most_common(1)

def most_comm():
    for txt in list_txt():
       print wc(txt)

if __name__ == "__main__":
    most_comm()
