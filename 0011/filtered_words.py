#!/usr/bin/env python

def filtered_words(f_file):
    filtered_list = []
    with open(f_file,'r') as f:
        for line in f:
            filtered_list.append(line.strip())
    return filtered_list

def filtered_or_not(input_word,f_file):
    return (input_word in filtered_words(f_file)) 

def print_user_input(input_word,f_file):
    if filtered_or_not(input_word,f_file):
        return "Freedom"
    return "Human Rights"

if __name__ == "__main__":
    input_word = raw_input("please input your word:")
    f_file = "filtered_words.txt"
    print print_user_input(input_word,f_file)
