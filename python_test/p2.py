import random
import string

def gen_activation_code(id,length = 12):
	'''
		产生激活码
	'''

	prefix = hex(int(id))[2:] + 'h'
	#print(prefix)
	foo = hex(int(id))
	#print(foo)
	#print foo[0],foo[1]
	length = length - len(prefix)
	chars = string.ascii_letters + string.digits
	activation_code = prefix + ''.join([random.choice(chars) for i in range(length)])
	return activation_code
	
def hex_to_dec(hex_num):
	return int(hex_num.upper(),16)
	

if __name__  == '__main__':
	for i in range(10,300,15):
		code = gen_activation_code(i)
		id_hex = code.split('h')[0]
		id = hex_to_dec(id_hex)
		#print type(id)
		print code,id
		
		
		