from collections import deque
class Node:
   def __init__(self,data):
       self.data=data
       self.left=None
       self.right=None
class TreeNode:
   def __init__(self):
       self.root=None
   def append(self,data):
       newNode=Node(data)
       if self.root==None:
           self.root=newNode
       else:
           temp=self.root
           while True:
               if data<temp.data:
                   if temp.left!=None:
                       temp=temp.left
                   else:
                       temp.left=newNode
                       break
               else:
                   if temp.right!=None:
                       temp=temp.right
                   else:
                       temp.right=newNode
                       break
                   
   def bfs(self, root):
       list = []
       if root is None:
           print("Sum: 0")
           return
       queue = deque()
       queue.append(root)
       total = 0
       while queue:
           temp = queue.popleft()
           list.append(temp.data)
           if temp.left:
               queue.append(temp.left)
           if temp.right:
               queue.append(temp.right)
       print(list)
       list.sort()
       print(list) 
       lst = list  
       target = 130            
       left = 0
       right = len(lst) - 1
       found = False
       while left < right:
           current_sum = lst[left] + lst[right]
           if current_sum == target:
               print([lst[left], lst[right]],end=" ")
               left += 1
               right -= 1
               found = True
           elif current_sum < target:
               left += 1
           else:
               right -= 1
       if not found:
           print("No pair found")
                   
if __name__=='__main__':
   tree=TreeNode()
   while True:
       data=int(input("Enter data "))
       if data>0:
           tree.append(data)
       else:
           break
   tree.bfs(tree.root)

