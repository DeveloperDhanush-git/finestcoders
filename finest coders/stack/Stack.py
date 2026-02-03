class Node:
    def __init__(self,data):
        self.data = data
        self.add = None
class Stack:
    def __init__(self):
        self.head = None
    def append(self,data):
        newnode = Node(data)
        newnode.add = self.head
        self.head = newnode
    def display(self):
        temp = self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp = temp.add

if __name__ == "__main__":
        list = Stack()
        while True:
            data = int(input())
            if data >=0:
                list.append(data)
            else:
                break
list.display()