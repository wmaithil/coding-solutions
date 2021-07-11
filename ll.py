class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def insertTop(self,data):
        if self.head == None:
            self.head=Node(data)
            
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode

    def insertL(self,data):
        if self.head == None:
            self.head=Node(data)
            return
        
        temp=self.head
        while(temp.next):
            temp=temp.next
        #reached last Node 
        newNode=Node(data)
        temp.next=newNode

    def insert(self,pos,data):
        temp=self.head
        #If position is 1 i.e, head
        if(pos==1):
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode

        count=1  
        while(count<pos-1 and temp.next):
            temp=temp.next
            count+=1

        newNode=Node(data)
        newNode.next=temp.next
        temp.next=newNode

    def remove(self,pos):
        temp=self.head

        if(pos == 1):
            self.head=temp.next
            del(temp)
        
        count=1  
        while(count<pos-1 and temp.next):
            temp=temp.next
            count+=1
        temp.next=temp.next.next

    def pop(self):
        if(self.head==None):
            print("List empty")
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        del(temp.next)
        temp.next=None 

    def printList(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" -->",end=" ")
            temp=temp.next
        print("None")

#-----------------------------    
l1=LinkedList()
l2=LinkedList()

l1.insertTop(5)
l1.printList()
l2.printList()


for a in range(2,6):
    l1.insertL(a)
print("Printink l1 :")
l1.printList()

l1.insertL(6)
print("Printink l1 :")
l1.printList()

l1.insertL(7)
print("Printink l1 :")
l1.printList()

l1.remove(3)
print("Printink l1 :")
l1.printList()

l1.insert(3,3)

l1.pop()
print("Printink l1 :")
l1.printList()

for a in range(2,6):
    l2.insertL(a)
print("Printink l2 :")
l2.printList()

        


       


