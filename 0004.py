#!/usr/bin/env python

import collections
import re

def wc(filename):
    datalist = []
    with open(filename,'r') as f:
        for line in f:
             content = re.sub("\"|,|\.","",line)
             datalist.extend(content.strip().split(' '))
    #print datalist
    print collections.Counter(datalist)

if __name__ == "__main__":
    filename =  'test.txt'
    wc(filename)
