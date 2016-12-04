#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 任一个英文的纯文本文件，统计其中的单词出现的个数.
import sys

def count_words(text):
    file = open(text, "r")
    counts = {}
    for word in file.read().split():
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    file.close()
    return counts

if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        counts = count_words(sys.argv[i])
        print "-------%s-------" %(sys.argv[i])
        for key in sorted(counts.keys()):
            print "{}\t{}".format(key, counts[key])


