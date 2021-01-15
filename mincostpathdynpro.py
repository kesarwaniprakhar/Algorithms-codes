# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:10:49 2019

@author: prakhar prakash
"""

mat1 = [[1,2,3],[4,8,2],[1,5,3]]

m = int(input('Enter the value of m'))
n = int(input('Enter the value of n'))

def mincostpath(mat1,m,n):
    
    dp = [[0 for x in range(len(mat1[0]))] for x in range(len(mat1)) ]
    
    dp[0][0]  = mat1[0][0]    
    
    for j in range(1,len(mat1[0])):  #loop for first row and all columns
        dp[0][j] = mat1[0][j] + dp[0][j-1]
        
    for i in range(1,len(mat1)):     # loop for first column and all rows
        dp[i][0] = mat1[i][0] + dp[i-1][0]
        
    for i in range(1,len(mat1)):
        for j in range(1,len(mat1[0])):   #both loop for other than first row, all columns and first columns, all rows. 
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + mat1[i][j]
        
    return dp[m][n]    

print(mincostpath(mat1,m,n))