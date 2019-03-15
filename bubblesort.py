# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 18:05:04 2019

@author: prakhar prakash
"""

list1 = list()
size = int(input('Enter the size of the list'))
for r in range(size):
    list1.append(r)
    list1[r] = int(input('Enter the value at location ' + str(r) + ':'))

print(list1)    



def bubble(list1):
    istrue = False
    n = len(list1)-1          #this is optimised implementation
    while not istrue:
        istrue = True
            
        for r in range(n):
            if list1[r] > list1[r+1]:
            
                temp = list1[r]
                list1[r] = list1[r+1]
                list1[r+1] = temp
                istrue = False
            
        n -= 1    

        
        
        
bubble(list1)
print(list1)        
    
    