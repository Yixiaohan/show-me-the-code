#-*-coding: utf-8-*-
import uuid
class generate_N_keys:
	def __init__(self):
		self.Num=0
		self.list=[]

	def generate(self,Num):
		for i in range(Num):
			self.list.append(uuid.uuid1())

	def return_list(self):
		return self.list


test=generate_N_keys()
test.generate(200)
keys=test.return_list()
print(keys)
print(len(keys))
# 转换为字典看keys 是否也是200，表明其中是否有重
print(len({}.fromkeys(keys).keys()))
# 注释掉的是两种存储方法一种是pickle.dump序列化的方法；另外一种是保存原文的方法
##part 01
# import pickle
# with open('keys.txt','wb') as f:
# 	pickle.dump(keys,f)
## pickle.load(keys.txt)

## part 02
# with open('keys.txt','w') as f:
# 	f.writelines("%s\n"%item for item in keys)

# with open('keys.txt','r') as f:
# 	keys_ag=f.readlines()

# keys_ag_ag=[]
# for keys_name in keys_ag:
# 	keys_name=keys_name.replace('\n','')
# 	keys_ag_ag.append(keys_name)

# print(keys_ag_ag)