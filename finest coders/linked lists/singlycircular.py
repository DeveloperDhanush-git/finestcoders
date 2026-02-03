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
            while temp.add!=self.head:
                temp = temp.add
            temp.add = newnode
        newnode.add=self.head
    
    def display(self):
        r=1
        temp=self.head
        while temp!=self.head or r==1:
            r=0
            print(temp.data,end=" ")
            temp = temp.add
        print()
        
    def display_from_k(self, k):
        temp = self.head
        count = 1
        while count < k:
            temp = temp.add
            count += 1
        start = temp
        while True:
            print(temp.data, end=" ")
            temp = temp.add
            if temp == start:
                break
        print()

if __name__ == "__main__":
    clist = SinglyLinkedlist()
    while True:
        data = int(input("Enter data (negative to stop): "))
        if data >= 0:
            clist.append(data)
        else:
            break
    k = int(input())
    clist.display()
    clist.display_from_k(k)