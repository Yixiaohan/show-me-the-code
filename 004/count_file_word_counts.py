#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, os.path
import re
import sys, getopt

other = ['.', '_', '#', '/', '(', ')', '#', '-', '\"', '\'']

def word_count(filePath):
    count = 0
    if os.path.isfile(filePath):
        with open(filePath, 'r') as f:
            for l in f:
                pattern = re.compile(r'^[a-zA-Z]*', re.I|re.M)
                for t in other:
                    l = l.replace(t, ' ')
                l1 = l.split()
                for s in l1:
                    if pattern.fullmatch(s):
                        count += 1
        return count
    else:
        print("NOT a file, please input a path of file")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "-h-i:-o:",["--help", "--input=","--output="])
    except getopt.GetoptError:
        print("run <filename>.py -i <inputFile> -o <outputFile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("run <filename>.py -i <inputFile> -o <outputFile>")
        if opt == '-i':
            inputfile = arg
        if opt == '-o':
            outputfile = arg

    count = word_count(inputfile)
    with open(outputfile, 'w') as outF:
        outF.write("The file in ")
        outF.write(inputfile)
        outF.write(" has ")
        outF.write(str(count))
        outF.write(" words!\n")
    print('The file in', inputfile, 'has', count, 'words!')

if __name__ == '__main__':
    main(sys.argv[1:])
