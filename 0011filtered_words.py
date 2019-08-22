import os
import re



def fileter(str):
    for each in words:
        if not str.find(each)==-1:
            print('Freedom')
            return True
    print('Human Rights')
    return False

with open('filtered_words.txt', 'r', encoding='utf-8') as k:
    words = k.read().splitlines()
    k.close()

word=''
while not word.upper()=="EXIT":
    word=input('输入敏感词:')
    fileter(word)
