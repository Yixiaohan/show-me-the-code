#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
# 例如当用户输入「北京是个好城市」，则变成「**是个好城市」。


def f_words(f_file):
    filtered_list = []
    with open(f_file, 'r') as f:
        for line in f:
            filtered_list.append(line.strip())
    return filtered_list


def filtered_or_not(f_word, input_str):
    return (f_word in input_str)


def f_replace(f_word, input_str):
    return input_str.replace(f_word, "**")


def main(f_file, input_str):
    f_words_list = f_words(f_file)
    for f_word in f_words_list:
        if filtered_or_not(f_word, input_str):
            input_str = f_replace(f_word, input_str)
    return input_str


if __name__ == "__main__":
    input_str = raw_input("please input your string:")
    f_file = "filtered_words.txt"
    print main(f_file, input_str)
