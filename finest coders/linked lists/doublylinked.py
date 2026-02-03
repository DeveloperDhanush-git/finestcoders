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
            while temp.right!=None:
                temp = temp.right
            temp.right = newnode
            newnode.left = temp
    def displayforward(self):
        temp = self.head
        print("forward traversal")
        while temp!=None:
            print(temp.data,end=" ")
            temp = temp.right
        print()
    def displayback(self):
        temp = self.tail
        print("reverse traversal")
        while temp!=None:
            print(temp.data,end=" ")
            temp = temp.left
            
if __name__ == "__main__":
    list = doublyLinkedlist( )
    while True:
        data = int(input())
        if data>=0:
            list.append(data)
        else:
            break 
list.displayforward()
list.displayback()
