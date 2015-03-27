import os


path = 'C:\Users\pc\study'
re_pre = [',', '.', ':', '"', '"', '?', '!', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def count_words(a_path):
	dict = {}
	with open(a_path,'r') as f:
		text = f.read()
		for i in re_pre:
			text = text.replace(i,' ')
		words_list = text.split(' ')
	for word in words_list:
		if word in dict:
			dict[word] += 1
		elif word == ' ':
			continue
		else:
			dict[word] = 1
	max = 0 
	for k, v in dict.iteritems():
		if v >= max:
			max = v
			key_word = k
		else:
			continue
		
	return key_word

if __name__  ==  '__main__':
	diary_list = [x for x in os.listdir(path) if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt']
	for i in diary_list:
		a_path = os.path.join(path,i)
		print i,count_words(a_path)

	