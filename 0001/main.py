# coding = utf-8

import random, string

def getRandToken(length = 8):
	s = "abcdefghijklmnopqrstuvwxyz"
	s += s.upper()
	s += "0123456789"
	Token = ""
	for x in xrange(0,length):
		Token += s[random.randint(0,61)]
	return Token
def getRandToken_2(length = 8):
	chars = string.letters + string.digits
	Token = [random.choice(chars)for x in xrange(0,length)]
	return Token

if __name__ == '__main__':
	file = open("activate_code.txt", "w")
	length = 10
	for x in xrange(0,200):
		file.write("".join(getRandToken(length))+'\n')

	file.close()