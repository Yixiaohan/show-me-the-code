#!/bin/env python
#寻找n以内的素数，看执行时间，例子100000内的素数

def prime(n):
    all = range(n+1)
    flag = [1]*(n+2)
    flag[1] = 0		# 1 is not prime
    flag[n+1] = 1
    p=2
    while(p<=n):
        print p 
        i = 2*p    
        for i in range(n+1)[::p]: 
            flag[i] = 0
        while True:
            p += 1
            if(flag[p]==1):
                break
# test
prime(100000)   

# 9592 numbers        
# time
#real	0m58.866s
#user	0m58.286s
#sys	0m0.124s
