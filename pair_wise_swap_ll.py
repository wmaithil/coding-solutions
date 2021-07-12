"""  list Node

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping

def pairWiseSwap(head):
    # code here
    temp=0
    cur=head
    nxt=head.next
    while(cur!=None and nxt!=None):
        temp=cur.data
        cur.data=nxt.data
        nxt.data=temp
        cur=cur.next.next
        if(nxt.next):
            nxt=nxt.next.next
    return head
    




#{ 
#  Driver Code Starts


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = pairWiseSwap(lis.head)
        printList(head)
