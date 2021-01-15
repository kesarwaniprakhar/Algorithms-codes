newlist = [6,-2, 4, 3, -4, 5]

i = 0
j = 2
list1 = [0] * len(newlist)
print(list1)
m = newlist[0]
list1[0] = newlist[0]
list1[1] = newlist[1]

def MaxSum(newlist):
    global j,m,i
    for r in range(len(newlist) - 2):
        i = 0
        while i < j - 1:
            
            if (newlist[i] + newlist[j]) > list1[j]:
            
                list1[j] = newlist[i] + newlist[j]
                print(list1 ," ",newlist)
            
            if (list1[i] + newlist[j]) > list1[j]:
                list1[j] = list1[i] + newlist[j]
                print(list1 ," ",newlist)
           
            if m < list1[j]:
                m = list1[j]
            
            print(m)
            i += 1 
        j += 1 
    return m   
print(MaxSum(newlist))  

        
    


        
    
    
    
        
        
        
        
        
        
        
    
        
        
        
    
    
     

        
        
        
        
        
        
       
