 # -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:42:12 2019

@author: prakhar prakash
"""

list1 = 'atynji'
list2 = 'aytiu'

i,j = 0,0

def lcs(list1,list2,i,j):
    
    if i is len(list1) or j is len(list2):
        return 0
    elif list1[i] is list2[j]:
        return 1 + lcs(list1,list2,i+1,j+1)
    else:
        return max(lcs(list1,list2,i+1,j),lcs(list1,list2,i,j+1))
    
print('lcs is', lcs(list1,list2,i,j))           