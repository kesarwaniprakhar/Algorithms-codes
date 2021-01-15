# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:36:30 2019

@author: prakhar prakash
"""

N = 4
S = [1,23]
n = len(S)

def coinchange(S,n,N):
    
    dp = [[0 for x in range(N+1)] for x in range(n+1)]
    
    dp[0][0] = 1
    
    for j in range(1,N+1):  
        dp[0][j] = 0
    
    
    for i in range(1,n+1):
        for j in range(N+1):
            
            if j-S[i-1] < 0:
                
                withthisvalue = 0
            else:
                withthisvalue = dp[i][j-S[i-1]]
                
            withoutthisvalue = dp[i-1][j]
            
            dp[i][j] = withthisvalue + withoutthisvalue
            
    return dp[i][j]

print(coinchange(S,n,N))    
            
    