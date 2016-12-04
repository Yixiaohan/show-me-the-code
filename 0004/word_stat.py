#-*- coding:utf-8-*-

with open('test.txt', 'r') as f:
    from collections import Counter
    c = Counter()
    for line in f:
        words = line.split()
        print(words)
        c += Counter(words)
    print(c)
