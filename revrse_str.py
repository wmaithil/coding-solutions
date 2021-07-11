inp=list(input("Enter String "))
l=len(inp)
i=0
j=l-1
while(i<j):
    inp[i],inp[j]=inp[j],inp[i]
    i+=1
    j-=1

print("reversed string is :")
for i in inp:
    print(i,end="")
print("\n")
