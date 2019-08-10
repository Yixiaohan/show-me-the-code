import jieba
import re
def eng_split():
    r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~]+'
    list=[]
    with open('english.txt','r') as w:
        res=w.read()
    res=re.sub(r,'',res)
    list.extend(res.split())
    tf={}
    for each in list:
        each=each.lower()
        if not each in tf:
            tf[each]=1
        else:
            tf[each]+=1
    for each in tf.items():
        print(each[0],each[1])
    return tf

'''
英文的分词比中文的分词简单太多
具体做法是
1.使用正则表达式去除标点符号
2.使用split()方法根据空格分词
3.利用字典对数组中的每一个元素进行遍历
'''
eng_split()
