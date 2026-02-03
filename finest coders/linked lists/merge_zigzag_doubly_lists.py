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
       temp1=self.head1
       temp2=self.head2
       while temp1 and temp2:
           ptr1=temp1.right
           ptr2=temp2.right
           temp1.right=temp2
           temp2.left=temp1
           if ptr1 != None:
               temp2.right=ptr1
               ptr1.left=temp2
           temp1=ptr1
           temp2=ptr2
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
   list.merge()
   list.display(list.head1)
