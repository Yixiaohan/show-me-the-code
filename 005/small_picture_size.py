#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, os.path
import re
import sys, getopt
import glob
import PIL
from PIL import Image


def picture_size(inputFile, size):
    #
    #res = outputFile
    size *=1024*1024
    pwd = os.getcwd()
    path = inputFile
    res = "results"
    #if not os.path.isdir(res):
    #    os.makedirs(res)
    #else:
    #    os.chdir(res)
    #    for ns in glob.glob('*out'):
    #        os.remove(ns)
    os.chdir(pwd)
    if os.path.isdir(path):
        os.chdir(path)
        for ns in glob.glob('*out'):
            os.remove(ns)
        for name in glob.glob('*.jpg'):
            filesize = os.path.getsize(name)
            q = 100
            if filesize > size :
                outf ='out' + name
                img = Image.open(name)
                while filesize > size and q >0:
                    q = q -5
                    out = img.resize(img.size, Image.ANTIALIAS)
                    out.save(outf, 'JPEG', quality=q)
                    filesize = os.path.getsize(outf)


def main(argv):
    inputfile = ''
    size = 0
    try:
        opts, args = getopt.getopt(argv, "-h-i:s:",["--help", "--input=", "--size="])
    except getopt.GetoptError:
        print("run <filename>.py -i <inputFile> -s <size>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("run <filename>.py -i <inputFile> -s <size>")
        if opt == '-i':
            inputfile = arg
        if opt == '-s':
            size = arg

        picture_size(inputfile, size)

if __name__ == '__main__':
    main(sys.argv[1:])
