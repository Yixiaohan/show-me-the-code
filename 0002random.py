import random
import string
def genernate_key(number=5,lenth=8,part=4):
    result=[]
    char_set=string.ascii_letters + string.digits
    #char_set="abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(0,number):
        key=''
        for j in range(0,part):
            for k in range(0,lenth):
                key=key+random.choice(char_set)
            key=key+'-'
        key=key[0:-1]
        if key not in result:
            result.append(key)
            print("%s %s"%(str(i+1),key))
        else:
            i-=1
    with open('keys.txt','a') as w:
        for each in result:
            w.write(each+'\n')
    return result

def key_read():
    result=[]
    f=open('keys.txt','r')
    for lines in open('keys.txt','r'):
        result.append(lines[0:-1])
    return result

def verify_key(result,key):
    if key in result:
        result.remove(key)
        return True
    else:
        return False
    
#genernate_key()
result=key_read()
key='yf56g7h8-cot4imw3-9e01gml1-0gy7xkdi'
print(verify_key(result,key))
