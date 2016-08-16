#Filename:2.py
#-*- coding:utf-8 -*-

import random
import redis

char = "1234567890poiuytrewqasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM"

def get_coupon(length, char):
	coupon = ""
	for i in range(0, length):
		coupon = coupon+random.choice(char)
	return coupon

def save_coupon(num, coupon):
	r = redis.StrictRedis(host="localhost", port=6379, db=0)
	r.set(num, coupon)

def main():
	length = int(raw_input("input length of the coupon:"))
	num = 20
	for i in range(0,num):
		coupon = get_coupon(length, char)
		save_coupon(i, coupon)

if __name__ == '__main__':
	main()


