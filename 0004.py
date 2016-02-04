#!/usr/bin.env python

import sys

def WordCounter():
	dict = {}
	t = ',.:?\'\"'

	f = open("english.txt", 'r')
	lines = f.readlines()
	for line in lines:
 		for i in t:
 			line = line.replace(i, '')
 		for word in line.split():
 			if word in dict:
 				dict[word] += 1
 			else:
 				dict[word] = 1

 	for key, value in dict.items():
 		print '(%s, %d)' %(key, value)


if __name__ == '__main__':
	WordCounter()

