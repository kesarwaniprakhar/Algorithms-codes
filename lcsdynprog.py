# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 16:49:37 2019

@author: prakhar prakash
"""

str1 = 'atyunji'
str2 = 'aytiu'

m,n = len(str1),len(str2)

def lcs(str1,str2,m,n):
     
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            
            if i is 0 or j is 0:
                dp[i][j] = 0
            
            elif str1[i-1] is str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] 
            
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    
    return dp[m][n]           


print(lcs(str1,str2,m,n))                