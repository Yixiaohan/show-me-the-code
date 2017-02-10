# -*- coding:utf-8 -*-

words = open('filtered_words.txt').read().split()
word = input("Please input a word:\n")
if word in words:
    print("Freedom")
else:
    print("Human Rights")
