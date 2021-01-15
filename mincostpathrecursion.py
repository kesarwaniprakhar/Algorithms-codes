# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:59:42 2019

@author: prakhar prakash
"""

mat1 = [[1,15,3],[4,8,2],[1,5,3]]

i = int(input('Enter the value of i'))
j = int(input('Enter the value of j'))


def mincostpath(mat1,i,j):
    if i==0 and j==0:
        return mat1[0][0]
    elif i==0:
        return mat1[i][j] + mincostpath(mat1,i,j-1)
    elif j==0:
        return mat1[i][j] + mincostpath(mat1,i-1,j)
    
    else:
        return mat1[i][j ]+ min(mincostpath(mat1,i,j-1),mincostpath(mat1,i-1,j),mincostpath(mat1,i-1,j-1))
    
print(mincostpath(mat1,i,j))    
