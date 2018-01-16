#生成200个优惠卷，每个优惠卷由20个字母和数字组成

import string 
import random
#大小写字母从string模块的类变量中取
def generate_discout_code(count,lenght=20):
	letters=string.ascii_letters+'0123456789'
	
	for i in range(count):
		discount_code=''
		for j in range(lenght):
			discount_code+=random.choice(letters)
		print (discount_code)

if __name__ == '__main__':
	generate_discout_code(200)
