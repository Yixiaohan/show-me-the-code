#! usr/bin/python3
"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。
"""

class PyfileInfo:

    def __init__(self, file):
        self.file_name = file
        self.total_line_num = 0
        self.blank_line_num = 0
        self.comment_line_num = 0
        
    def count_lines(self):
        if self.file_name[-3:] != '.py':
            print(self.file_name + ' is not a .py file!')
            return
        mc_flag = False
        mc_start = ''
        """
        最高优先级检测由三连引号包围的多行注释，也可能是单行注释；
        其次检测空行；
        再次检测由#开头的单行注释，由单引号或者双引号包围的单行注释；
        """
        try:
            with open(self.file_name) as code:
                for each_line in code:
                    self.total_line_num += 1
                    temp = each_line.strip()
                    if mc_flag is False:
                        if temp[0:3] in ["'''", '"""']:
                            mc_start = temp[0:3]
                            mc_flag = True
                            if len(temp) >= 6 and temp[-3:] == mc_start:
                                self.comment_line_num += 1
                                mc_start = ''
                                mc_flag = False
                        else:
                            if len(temp) == 0:
                                self.blank_line_num += 1
                            else:                                
                                if temp[0] == '#':
                                    self.comment_line_num += 1
                                elif temp[0] in ['"', "'"] and temp[0] == temp[-1:]:
                                    self.comment_line_num += 1                                
                    elif temp[-3:] == mc_start:
                        #found the end of the multiple-line comment
                        self.comment_line_num += 1
                        mc_start = ''
                        mc_flag = False
                    if mc_flag:
                        self.comment_line_num += 1
        except IOError as err:
            print('File error: ' + str(err))

    def display(self):
        print('-.' * 15)
        print('The ' + self.file_name + ' code statistic is:')
        print('Total line number is:', self.total_line_num)
        print('Blank line number is:', self.blank_line_num)
        print('Comment line number is:', self.comment_line_num)

import os

target_path = 'program'
#Get file list from the target directory excluding files in its subdirectories
file_list = [f for f in os.listdir(target_path)
             if os.path.isfile(os.path.join(target_path, f))]
#Get .py file list 
pyfile_list = [os.path.join(target_path, f) for f in file_list
               if f[-3:] == '.py']

Total_line_num = 0
Blank_line_num = 0
Comment_line_num = 0

print('==' * 32)
for each_file in pyfile_list:
    py_file = PyfileInfo(each_file)
    py_file.count_lines()
    py_file.display()
    Total_line_num += py_file.total_line_num
    Blank_line_num += py_file.blank_line_num
    Comment_line_num += py_file.comment_line_num

print('=-' * 24)
print('All code files in ' + target_path + ' statistic is:')
print('Total line number is:', Total_line_num)
print('Blank line number is:', Blank_line_num)
print('Comment line number is:', Comment_line_num)
