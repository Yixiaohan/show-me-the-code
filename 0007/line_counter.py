"""
    有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
    包括空行和注释，但是要分别列出来。
"""
# -*- coding:gbk -*-
import os
import re

root_dir = os.getcwd() + "/program"
os.chdir(root_dir)

code_count = 0
note_count = 0


def isnote(line):
    line = line.strip()
    #print(line, line_count)
    if len(line) >= 2:
        # print("***")
        print("&&&", line[0], line[1])
        if line[0] == 47 and line[1] == 47:
            return "//"
        elif line[0] == 47 and line[1] == 42:
            return "/*"
        else:
            return "no"

for parent, dirnames, filenames in os.walk(root_dir):
    #print(parent, filenames)
    # print(dirname)

    for filename in filenames:
        os.chdir(parent)
        # print(filename)
        # print(parent)
        with open(filename, "rb") as f:
            line = f.readline().strip()
            while line != b"":
                # print("*")
                ret = isnote(line)
                # print(ret)
                if ret == "//":
                    note_count = note_count + 1
                elif ret == "/*":
                    line = f.readline().strip()
                    # print(line)
                    # if len(line) >= 2:
                    while b"*/" in line:
                        note_count = note_count + 1
                        line = f.readline().strip()
                        # print(line)
                elif ret == "no":
                    code_count = code_count + 1
                line = f.readline().strip()

print("代码行数:%d" % code_count)
print("注释函数 %d" % note_count)
