# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:59:54 2019

@author: prakhar prakash
"""

str1 = 'cat'
str2 = 'put'

def editdis(str1,str2,m,n):
    
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            
            if i is 0:
                dp[i][j] = j
                
            if j is 0:
                dp[i][j] = i
            
            if str1[i-1]==str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                
            else:
                dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[m][n]

print(editdis(str1,str2,len(str1),(len(str2))))
            
            
    
    
