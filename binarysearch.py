# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:06:28 2019

@author: prakhar prakash
"""

size = int(input('Enter the size of the list'))
list1 = []
for r in range(size):
    list1.append(r)
    list1[r] = int(input('Enter the value at position in ascending order' + str(r) + ": "))
print(list1)    
first = 0
last = size-1
mid = (first+last)//2

num = int (input('Enter the number to be searched in the list'))


while first <= last:
   # print(num)
    mid = (first+last)//2
    if list1[mid] is num:
        print('Number found at position ' + str(mid))
        break
    elif list1[mid] < num:
        first = mid + 1
    else:
        last = mid - 1

if list1[mid] is not num:
    print('Number is not present')        
