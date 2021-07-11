class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None 

class DLinkList:

    def __init__(self):

        self.head=None 

    def inserthead(self,data):
        if self.head == None:
            self.head=Node(data)
        else:
            temp=self.head
            newNode=Node(data)
            newNode.next=temp.next
            newNode.prev=None 
            del(temp)

    def append(self, data):
        temp=self.head
        while(temp.next):
            temp=temp.next
        #append Node at last
        newNode=Node(data)
        newNode.prev=temp
        temp.next=newNode

    def pop(self):
        temp=self.head
        if(temp.next==None):
            self.head=None
            del(temp)
            return

        while(temp.next.next):
            temp=temp.next
        #append Node at last
        del(temp.next)
        temp.next=None

    def printList(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" -->",end=" ")
            temp=temp.next
        print("None")
# Main program
l1=DLinkList()
l2=DLinkList()

l1.inserthead(5)
l1.printList()

l2.inserthead(4)
l2.printList()

for i in range(1,4):
    l1.append(i)
l1.printList()

l1.pop()
l1.printList()

l1.append(24)
l1.printList()


        



