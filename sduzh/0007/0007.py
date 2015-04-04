#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys

def flines(fname):
	try:
		file = open(fname, 'r')
		lines = file.readlines()
		nblank = sum(1 for line in lines if line.isspace())
		mcomment = sum(1 for line in lines if line.strip().startswith('//'))
	finally:
		file.close()

if __name__ == '__main__':
	count_lines(os.path.join(os.getcwd(), sys.argv[0]))

