#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


def filtered_words(f_file):
    filtered_list = []
    with open(f_file, 'r') as f:
        for line in f:
            filtered_list.append(line.strip())
    return filtered_list


def filtered_or_not(input_word, f_file):
    filtered_words_list = filtered_words(f_file)
    return (input_word in filtered_words_list)


def print_user_input(input_word, f_file):
    if filtered_or_not(input_word, f_file):
        return "Freedom"
    return "Human Rights"


if __name__ == "__main__":
    input_word = raw_input("please input your word:")
    f_file = "filtered_words.txt"
    print print_user_input(input_word, f_file)
