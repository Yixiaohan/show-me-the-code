# -*- coding: utf-8 -*-
import redis

def storeInRedis(filepath):
	r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
	r.flushdb()
	file = open(filepath, 'rb')
	f = file.readlines()
	for line,num in zip(f, xrange(1, len(f)+1)):
		code = line.strip()
		r.set(num, code)
def searchInRedis():
	id = int(input("input the id:\n"))
	r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
	result = r.get(id)
	print result

if __name__ == '__main__':
	filepath = "../0001/activate_code.txt"
	storeInRedis(filepath)
	searchInRedis()