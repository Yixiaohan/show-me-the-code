# -*- coding:utf-8 -*-

words = open("filtered_words.txt").read().split()
in_word = input("Please input an sentence:\n")
for w in words:
    in_word = in_word.replace(w, "*" * len(w))
print(in_word)
