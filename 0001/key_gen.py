#!/usr/bin/env python

import string
import random

KEY_LEN = 20
KEY_ALL = 200

def base_str():
    return (string.letters+string.digits)

def key_gen():  
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))

def key_num(num,result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(key_gen())
    return result

def print_key(num):
    for i in key_num(num):
        print i

if __name__ == "__main__":
    print_key(KEY_ALL)
    
