import os
import re

def get_txt(path):
    f_path=[]
    for root, dirs, files in os.walk(path):
        print(root,"\n",dirs,"\n",files)
        for f in files:
            if f.lower().endswith(".txt"):
                f_path.append(os.path.join(root,f))
    return f_path

def text_analysis(f_path):
    word_dic = {}
    f=open(f_path)
    text=f.read()
    word_list=re.findall(r'[a-zA-Z]+',text)
    print(word_list)
    for w in word_list:
        if w in word_dic:
            word_dic[w]+=1
        else:
            word_dic[w]= 1
    sort_wordic=sorted(word_dic.items(),key=lambda item:item[1])
    print(sort_wordic)
    print("在文件%s中，关键词为%s，出现次数为%s"%(os.path.basename(f_path),sort_wordic[-1][0],sort_wordic[-1][1]))

if __name__ == '__main__':
    for file in get_txt(os.getcwd()):
        text_analysis(file)


