# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:43:40 2019

@author: prakhar prakash
"""

list1 = [3,10,2,1,20]
#print(list1[0])
LIS = [1]*len(list1)


for i in range(1,len(list1)):
    for j in range(i):
        print(i,j)
        
        if list1[i] > list1[j] and LIS[i] <= LIS[j]:
            LIS[i] = 1 + LIS[j]
            print(LIS[i])
            
            
print(max(LIS))            
            
            
        

    