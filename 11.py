#Filename:11.py
#-*- coding:utf-8 -*-
def read_fuck_words(filename):
	txt = open(filename, 'r')
 	words = txt.readlines()
 	fuck_words = []
 	for word in words:
 		word = word.strip('\n')
 		fuck_words.append(word)

	return fuck_words

def replace_fuck_words(words):
	input_word = raw_input()
	if input_word in words:
		print "Freedom"
	else:
		print "Human Rights"

def main():
	filename = "filtered_words.txt"
	fuck_words = read_fuck_words(filename)
	replace_fuck_words(fuck_words)


if __name__ == '__main__':
	main()