class Node:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
class LinkedList:
   def __init__(self):
       self.head1 = None
       self.head2 = None
   def append(self, data,head):
       newnode = Node(data)
       if head is None:
           head = newnode
       else:
           temp = head
           while temp.right!=None:
               temp = temp.right
           temp.right = newnode
           newnode.left = temp
       return head
   def display(self,head):
       while head:
           print(head.data, end=" ")
           head = head.right
       print()
   def merge(self):
       if self.head1 is None:
           self.head1 = self.head2
           return
       if self.head2 is None:
           return
       temp1 = self.head1
       while temp1.right is not None:
           temp1 = temp1.right
       temp1.right = self.head2
       self.head2.left = temp1
    
if __name__ == "__main__":
   list=LinkedList()
   print("Enter the data for first list")
   while True:
       data=int(input())
       if data>=0:
           list.head1=list.append(data,list.head1)
       else:
           break
   print("Enter the data for second list")
   while True:
       data=int(input())
       if data>=0:
           list.head2=list.append(data,list.head2)
       else:
           break

   print("first list data")
   list.display(list.head1)
   print("second list data")
   list.display(list.head2)
   print("merged list at last")
   list.merge()
   list.display(list.head1)
