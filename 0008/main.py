#coding = utf-8
import re

def getContent(filepath):
	html = open(filepath, "r")
	html = html.read()
	pattern = re.compile(r"<.+?>(.+)<.+?>")
	result = pattern.search(html)
	print result

if __name__ == '__main__':
	filepath = "./QingA.html"
	getContent(filepath)