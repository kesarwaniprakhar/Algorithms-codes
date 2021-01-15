# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 23:40:13 2019

@author: prakhar prakash
"""

n = int(input('Enter the position upto which find fibonacci series'))

def fib(n):
    dp = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            #print(i)
            dp[i] = 0
            #print(dp[i])
        
        
        
        
        if i == 1:
            #print(i)
            dp[i] = 1
            #print(dp[i])
            
       
        
        else:
            #print(i)
            dp[i] = dp[i-1] + dp[i-2]
        
        
    return dp[n-1]


print(fib(n))        
        
        