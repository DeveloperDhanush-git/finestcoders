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
                   
   def bfs(self,root):
        queue = deque()
        queue.append(root)
        while queue:
            temp = queue.popleft()
            print(temp.data,end=" ")
            if temp.left != None:
                queue.append(temp.left)
            if temp.right!= None:
                queue.append(temp.right)
    
                
       
    
if __name__=='__main__':
   tree=TreeNode()
   while True:
       data=int(input("Enter data "))
       if data>0:
           tree.append(data)
       else:
           break
   tree.bfs(tree.root)

