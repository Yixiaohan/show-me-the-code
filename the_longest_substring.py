#Filename:the_longest_substring.py
# -*- coding=utf-8 -*-
#给两个字符串A和B，找出A对于B的最长前缀。
#例：
#A: abcdeabcdesa
#B: description
#最长前缀：des

a = "abcdef"
b = 'bcfdf'
c = ''
num = []
for x in range(len(a)):
	c = c+a[x]
	if c in a:
		num.append(len(c))

print num[len(num)-1]