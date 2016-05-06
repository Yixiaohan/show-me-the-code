#!/bin/env python
#-*-coding:utf-8-*-
#寻找n以内的素数，看执行时间，例子100000内的素数
import sys

def prime(n):
    flag = [1]*(n+2)
    flag[1] = 0		# 1 is not prime
    flag[n+1] = 1
    p=2
    while(p<=n):
        print p 
        for i in xrange(2*p,n+1,p): 
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p]==1):
                break
# test
if __name__ == "__main__":
    n = int(sys.argv[1])
    prime(n)   

# n = 100000,find 9592 primes        
#$ time ./sushu.py 100000 |wc -l
#9592

#real	0m0.083s
#user	0m0.078s
#sys	0m0.009s
