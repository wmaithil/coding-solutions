open_list=["[","(","{"]
closed_list=["]",")","}"]
def check_p(l1):
    stack=[]
    
    if(len(l1)==0):
        return "None"
    else:    
        for i in l1:
            if(i in open_list):
                stack.append(i)
            elif(i in closed_list):
                pos=closed_list.index(i)
                if(len(stack)>0 and open_list[pos]==stack[len(stack)-1]):
                    stack.pop()
                else:
                    return "not balanced"
                
            
        if(len(stack)==0):
            return "balanced"
        else:
            return "not balanced"
        
        
t=int(input())
for _ in range(t):
    l=input()
    l1=[]
    for i in l:
        l1.append(i)
         
    op=check_p(l1)
    print(op)
