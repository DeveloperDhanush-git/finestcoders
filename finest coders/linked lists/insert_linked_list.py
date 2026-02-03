class Node:
    def __init__(self,data):
        self.data=data
        self.add=None

class SinglyLinkedlist:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.add!=None:
                temp = temp.add
            temp.add = newnode
    def insert(self,k):
        newnode = Node(k)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.add!=None:
                temp = temp.add
            temp.add = newnode
            
    def display(self):
        temp = self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp = temp.add

if __name__ == "__main__":
    list = SinglyLinkedlist( )
    while True:
        data = int(input())
        if data>=0:
            list.append(data)
        else:
            break
    k = int(input()) 

list.insert(k)
list.display()
