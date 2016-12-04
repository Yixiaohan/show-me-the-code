#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

import string
import random

KEY_LEN = 20
KEY_ALL = 200


def base_str():
    return (string.letters+string.digits)


def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))


def print_key(func):
    def _print_key(num):
        for i in func(num):
            print i
    return _print_key


@print_key
def key_num(num, result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(key_gen())
    return result


if __name__ == "__main__":
    # print_key(KEY_ALL)
    key_num(KEY_ALL)
