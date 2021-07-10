def sort012(arr,n):
    # code here
    dict={0:0,1:0,2:0}
    for i in range(n):
        if(arr[i]==0):
            dict[0]+=1
        elif(arr[i]==1):
            dict[1]+=1
        elif(arr[i]==2):
            dict[2]+=1 
    k=0
    for i in range(3):
        for _ in range(dict[i]):
            arr[k]=i
            #print(arr)
            k+=1
            
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split() ))
    sort012(arr,n)
    for i in range(n):
        print(arr[i],end=" ")
    print()
