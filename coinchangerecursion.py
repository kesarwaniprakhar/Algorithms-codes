# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
N = 4
S = [1,2,3]
n = len(S)

def coinchange(S,n,N):
    if N is 0:
        return 1
    
    elif n <= 0:
        return 0
    
    
    elif N <= 0  and n >= 0:
        return 0
    
    else:
        return coinchange(S,n-1,N) + coinchange(S,n,N-S[n-1])
    
    
print(coinchange(S,n,N))    
