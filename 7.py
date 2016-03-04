#Filename:7.py
#-*- coding:utf-8  -*-

filename = "1.py"
txt = open(filename, 'r')
lines = txt.readlines()

a = 0
b = 0
c = 0
for line in lines:
	if line[0] == '#':
		a+=1
	elif line == '\n':
		b+=1
	else:
			c+=1

print a,b,c
	
