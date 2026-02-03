class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class doublyLinkedlist:
    def __init__(self):
        self.head=None
        self.tail = None
    
    def append(self,data):
        newnode = Node(data)
        self.tail = newnode
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.right!=self.head:
                temp = temp.right
            temp.right = newnode
            newnode.left = temp
        newnode.right=self.head
        self.head.left=newnode
        
        
    def displayforward(self):
        temp = self.head
        r=1
        print("forward traversal")
        while temp!=self.head or r==1:
            r=0
            print(temp.data,end=" ")
            temp = temp.right
        print()
        
    def displayback(self):
        temp = self.tail
        r=1
        print("reverse traversal")
        while temp!=self.head.left or r==1:
            r=0
            print(temp.data,end=" ")
            temp = temp.left
        print()
        
    def display_from_kright(self, k):
        temp = self.head
        count = 1
        print("display from k in forward traversal:")
        while count < k:
            temp = temp.right
            count += 1
        start = temp
        while True:
            print(temp.data, end=" ")
            temp = temp.right
            if temp == start:
                break
        print()
        
    def display_from_kleft(self, k):
        temp = self.head
        count = 1
        print("display from k in reverse traversal:")
        while count < k:
            temp = temp.left
            count += 1
        start = temp
        while True:
            print(temp.data, end=" ")
            temp = temp.left
            if temp == start:
                break
            
if __name__ == "__main__":
    list = doublyLinkedlist()
    while True:
        data = int(input())
        if data>=0:
            list.append(data)
        else:
            break 
    k=int(input())
list.displayforward()
list.displayback()
list.display_from_kright(k)
list.display_from_kleft(k)
