# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:57:02 2019

@author: prakhar prakash
"""

size = int(input('Enter the size of array'))
list1 = []
for r in range(size):
    list1.append(r)
    list1[r] = int(input('Enter a number to enter at position ' + str(r)))
    
print(list1)


def linearsearch(listt,value):
    r = 0
    while listt[r] is not None:
        if listt[r] is value:
            return print('Element found at position' + str(r))
           # break
        #else:
            
         #   print('Element is not present in the list')
            
        r += 1
        return print('Element not present in list')
            
val = int(input('Enter an element to be searched in list'))
linearsearch(list1,val)            
            
    