# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:30:58 2019

@author: prakhar prakash
"""

A = list(map(int, input().split()))

def partition(A, start , end):
    pivot = A[start]
    i = start + 1
    j = end
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
           # print(i,'h')
        while i <= j and A[j] >= pivot:
            j -= 1
           # print(j)
        #print(i , ' ', j)    
        if i <= j:
            A[i] ,A[j] = A[j], A[i]
            
         #   print(A,'  k')
    #if i >= j:
    A[start], A[j] = A[j], A[start]
        
         
    #print(A)    
    return j    
    
    
def quicksort(A, start, end):
    if start < end:
        
        pindex = partition(A, start, end)
        #print(pindex)
        quicksort(A, start, pindex - 1)
        quicksort(A, pindex + 1, end)
        
    
quicksort(A, 0, len(A) - 1)    
print(A)      
        
        
    
           
            
            