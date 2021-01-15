

s = '{[()]}}}'

def isBalanced(s):
    l = []
    
    if s[0] is '}' or s[0] is ']' or s[0] is ')':
        return 'NO'    
    
    if len(s) % 2 == 0:
        for r in range(len(s)):
         
            if s[r] is '(' or s[r] is '{' or s[r] is '[':
                l.append(s[r])
        
            else:
                if ((len(l) == 0 and s[r] is ')') or (len(l) == 0 and s[r] is '}') or len(l) == 0 and s[r] is ']'):
                    return 'NO'  
                if s[r] is ']' and l[-1] is '[':
                    l.pop()
                elif s[r] is '}' and l[-1] is '{':
                    l.pop()
                elif s[r] is ')' and l[-1] is '(':
                    l.pop()
                else:
                    return 'NO'
        if len(l) == 0:
            return 'YES'
        else:
            return 'NO'                          
    else:
        return 'NO'

result = isBalanced(str(s))
print(result)
    

'''f = open('testfile.txt','r')       

f1 = f.readlines()


for s in f1:
    print((s))
    

    result = isBalanced(s)
    print(result)

#     fptr.write(result + '\n')
#
f.close()'''
