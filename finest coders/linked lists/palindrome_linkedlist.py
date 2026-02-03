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
        result = []
        while temp!=None:
            result.append(temp.data)
            print(temp.data,end=" ")
            temp = temp.right
        print()
        return result
    
    def displayback(self):
        temp = self.tail
        result = []
        while temp!=None:
            result.append(temp.data)
            print(temp.data,end=" ")
            temp = temp.left
        print()
        return result
    
if __name__ == "__main__":
    list = doublyLinkedlist()
    data = input("Enter a word: ")
    for char in data:
        list.append(char)
print("forward :")  
a=list.displayforward()
print("reverse :")
b=list.displayback()

if a == b:
    print("palindrome")
else:
    print("not a palindrome")
    