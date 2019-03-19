# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:28:35 2019

@author: prakhar prakash
"""

list1 = []
size = int(input('Enter the size of the list'))

for r in range(size):
    list1.append(r)
    list1[r] = int(input('Enter the value at location ' + str(r) + ':'))

print(list1)    



#temp = []
#for r in range(len(list1)):
 #   temp.append(r)
  #  temp[r] = 0
def sort(list1):
   
    
    if len(list1) > 1 :
        mid = len(list1)//2 
        leftarr = list1[:mid]
        rightarr = list1[mid:]
        sort(leftarr)
        #print(leftarr)
        sort(rightarr)
        #print(rightarr)
        merge(leftarr,rightarr,list1)
      
def merge(leftarr,rightarr,list1):
      
       
        i=j=k=0
        while i<len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                
                list1[k] = leftarr[i] 
                i += 1
            else:
                list1[k] = rightarr[j]
                j += 1
            k += 1        
                
        while i < len(leftarr):
            list1[k] = leftarr[i]
            i += 1
            k +=1
        while j < len(rightarr):
            list1[k] = rightarr[j]
            j += 1
            k+=1
            
        print(list1)    
  
             
sort(list1)
#print(list1)
