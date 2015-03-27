import string
__name__ = 'HameL'


f = open('test.txt','r')

text = f.read()

re_pre = [',', '.', ':', '"', '"', '?', '!', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in re_pre:
	text = text.replace(i,' ')
	
pre_wo = text.split(' ')

dict = {}

for j in pre_wo:
	if j in dict:
			dict[j] +=1
	if j == ' ':
			continue
	else:
			dict[j] = 1
			
for i in dict:
	print i,dict[i]




	
	

