#!/usr/bin.env python

import sys


def CalcWords():
    nums = 0
    f = open("english.txt", 'r')

    lines = f.readlines()
    for line in lines:
        for word in line.split():
            nums += 1

    return nums


if __name__ == '__main__':
    #print CalcWords()
    print len([x for lines in open('english.txt', 'r').readlines() for x in lines.split()])
