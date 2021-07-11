class mystack:
    def __init__(self):
        self.list=[]

    def push(self,data):
        self.list.append(data)

    def pop(self):
        a= self.list.pop()
        print("Popped element is ",a)
    
    def printstack(self):
        for i in self.list:
            print(i,end=" ")
        print("\n")
    
    def peek(self):
        le=self.list[-1]
        print("Stack Top contains :{}".format(le))
    
    def length(self):
        l=len(self.list)
        print("Length of Stack is ")
a=mystack()

for i in range(5):
    a.push(i)

a.pop()
a.peek()
a.printstack()


