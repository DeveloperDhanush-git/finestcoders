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
    def delete(self,start,end):
        temp = self.head
        diff = end-start
        while start>2:
            temp = temp.add
            start-=1
        ptr = temp
        while diff>=0:
            ptr = ptr.add
            diff-=1
        temp.add = ptr.add
            
            
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
    start = int(input()) 
    end = int(input())

list.delete(start,end)
list.display()
