# -*- coding:gbk -*-

import os


root_dir = os.getcwd() + "/program"
os.chdir(root_dir)

code_num = 0
comment_num = 0


def iscomment(line):
    print(line)
    if len(line) >= 2:
        if line[0] == 47 and line[1] == 47:
            return "//"
        elif line[0] == 47 and line[1] == 42:
            return "/*"
        else:
            return "no"


for parent, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        with open(filename, "rb") as f:
            line = f.readline().strip()
            while line != b'':
                ret = iscomment(line)
                if ret == "//":
                    comment_num += 1
                elif ret == "/*":
                    while b"*/" not in line:
                        comment_num += 1
                        line = f.readline().strip()
                    comment_num += 1
                else:
                    code_num += 1
                line = f.readline().strip()


print("Code Line Number:" + str(code_num))
print("Comment Line Number:" + str(comment_num))
