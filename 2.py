#Filename:2.py
#-*- coding:utf-8 -*-

import random

char = "1234567890poiuytrewqasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM"

def get_coupon(length, char):
	coupon = ""
	for i in range(0, length):
		coupon = coupon+random.choice(char)
	return coupon

def main():
	length = int(raw_input("input length of the coupon:"))
	num = 200
	for i in range(0,num):
		coupon = get_coupon(length, char)
		print coupon

if __name__ == '__main__':
	main()