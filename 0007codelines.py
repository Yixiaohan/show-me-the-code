import os

def read_codes(filepath):
    d = [j for j in os.listdir(filepath) if j.endswith('.py')]
    blank_lines=0
    total_lines=0
    note_lines=0
    for each in d:
        with open(filepath+'/'+each,'rb') as w:
            lines=w.readlines()
            total_lines+=len(lines)
            for per in lines:
                if per.startswith(bytes('#',encoding='utf-8')):
                    note_lines+=1
                if per==bytes('''\r\n''',encoding='utf-8'):
                    blank_lines+=1
    print('总代码行数：',total_lines)
    print('其中,注释行数：', note_lines)
    print('\t空白行数：', blank_lines)


read_codes('E:/Python学习之路/PYTHON每日刷题')
read_codes('E:/Python学习之路/独立完成空间爬虫')