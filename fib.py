def fact(a):
    if( a==1 ):
        return 1
    else:
        return (a* fact(a-1)


#num= int(input("Enter N ")) 
#r=int(input("Enter R"))

#print("Factorial of number is ", end=" ")
print( int(fact(5)) )