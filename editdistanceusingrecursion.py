# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 09:56:31 2019

@author: prakhar prakash
"""

str1 = 'cat'
str2 = 'put'

m = len(str1)
n = len(str2)

def editdis(str1,str2,m,n):
    if m is 0:
        return n
    if n is 0:
        return m
    if str1[m-1] is str2[n-1]:
        return editdis(str1,str2,m-1,n-1)
    else:
        return 1 + min(editdis(str1,str2,m,n-1), editdis(str1,str2,m-1,n), editdis(str1,str2,m-1,n-1))
    
print(editdis(str1,str2,m,n))    