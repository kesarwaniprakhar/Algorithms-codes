# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:29:29 2019

@author: prakhar prakash
"""

list1 = list()
size = int(input('Enter the size of the list'))
for r in range(size):
    list1.append(r)
    list1[r] = int(input('Enter the value at location ' + str(r) + ':'))

print(list1)  

def insertionsort(list1):
    
    for r in range(len(list1)):
        key = list1[r]
        s = r-1
        while(s >= 0 and key < list1[s]):
            #print(list1[s],list1[s+1])
            list1[s+1] = list1[s]
            list1[s] = key
           # print(list1[s],list1[s+1])
            
            s -= 1
            
            
        
        
        
        
insertionsort(list1) 
print(list1)       