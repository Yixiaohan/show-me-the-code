#coding:utf-8
import os

def get_py(path):
    f_path=[]
    for root, dirs, files in os.walk(path):
        print(root,"\n",dirs,"\n",files)
        for f in files:
            if f.lower().endswith(".py"):
                f_path.append(os.path.join(root,f))
    return f_path
def py_analysis(py_path,x,y,z):
    f=open(py_path,encoding='UTF-8')
    f=f.read()
    f=f.split("\n")
    N_um=0
    zhushi_line=0
    emptyline=0
    for line in f:
        N_um += 1
        if line.startswith('#'):
            zhushi_line +=1
        if line.startswith('\'\'\''):
            zhushi_line += 1
        if line.startswith('\"\"\"'):
            zhushi_line += 1
        if line.startswith(''):
            emptyline+=1
    print("在文件%s中，总数为%s行，注释行为%s，空行为%s" %(os.path.basename(py_path), N_um, zhushi_line, emptyline))
    return N_um,zhushi_line,emptyline
if __name__ == '__main__':
    total_num=0
    total_zhushi_line=0
    total_emptyline=0
    for file in get_py(os.getcwd()):
        b,c,d=py_analysis(file,x=0,y=0,z=0)
        total_num += b
        total_zhushi_line += c
        total_emptyline +=  d
    print("写入总数为%s行，注释行为%s，空行为%s" % (total_num, total_zhushi_line,total_emptyline))
