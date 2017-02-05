# -*- coding:utf-8 -*-

import random


def rand_series(count, len=10):
    str_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    series_set = set()
    i = 0
    while i < count:
        series = ''
        for j in range(0, len):
            series += random.choice(str_set)
        if series not in series_set:
            series_set.add(series)
            i += 1
            print(series)


rand_series(20)
