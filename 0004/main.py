# coding = utf-8
import re

def countWords(filepath):
	file = open(filepath, 'r')
	content = file.read()
	# pattern = re.compile(r'\b\w+?\b')
	# words = pattern.search(content)
	words = re.findall(r'\b\w+?\b', content)
	# print type(words)
	return len(words)


if __name__ == '__main__':
	filepath = "./passage.txt"
	print(countWords(filepath))