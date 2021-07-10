    n=len(height)
        
    if(n==0):
        return 0
        
    volum=0
    lmax=[0 for i in range(n)]
    lmax[0]=height[0]
        
    rmax=[0 for i in range(n)]
    rmax[n-1]=height[n-1]
            
    for i in range(1,n):
        temp=max(height[i],lmax[i-1])
        lmax[i]=temp
        
        
    for i in range(n-2,-1,-1):
        temp=max(height[i],rmax[i+1])
        rmax[i]=temp
        
        
    for i in range(1,n-1):
        volum=volum+min(lmax[i],rmax[i])-height[i]
            
        
    return volum;

tc=int(input())
for _ in range(tc):
    n=int(input())
    arr=list(map(int,input().strip().split() ))
    ans=trap(arr)
    print(ans)
