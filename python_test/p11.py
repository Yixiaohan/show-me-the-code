
input = raw_input("Please input the words:")

str_input = input.split(' ')

with open('filtered_words.txt','r') as f:
	list = f.read()
	for i in str_input:
		if i in list:
			print "Freedom"
		else:
			print "Human Rights"
			

	