
def kadanes(a,n):
    currmax=a[0]
    maxsofar=a[0]
    for i in range(1,n):
        currmax=max(a[i],currmax+a[i])
        maxsofar=max(maxsofar,currmax)
    return maxsofar

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().strip().split()))
    maxsum= kadanes(a,n)
    print(maxsum)
