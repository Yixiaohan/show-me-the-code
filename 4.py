#Filename:4.py
#-*- coding:utf-8 -*-

def split_word(filename):
	txt = open(filename)
	content = txt.read()
	words = content.split()
	return words

def get_num(words):
	num_words = {}
	for word in words:
		num_words[word] = words.count(word)
	return num_words

def sort_num(num_words):
	sorted_num = sorted(num_words.items(), key=lambda num_words:num_words[1], reverse=True)
	return sorted_num[0]

def main():
	filename = "test.txt"
	words = split_word(filename)
	num_words = get_num(words)
	sorted_num = sort_num(num_words)
	print sorted_num

if __name__ == '__main__':

	main()
	