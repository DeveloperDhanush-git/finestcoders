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
   def inOrderTraversal(self,root):
       if root==None:
           return
       self.inOrderTraversal(root.left)
       print(root.data,end=" ")
       self.inOrderTraversal(root.right)
       
   def preOrderTraversal(self,root):
       if root==None:
           return
       print(root.data,end=" ")
       self.inOrderTraversal(root.left)
       self.inOrderTraversal(root.right)
       
   def postOrderTraversal(self,root):
       if root==None:
           return
       self.inOrderTraversal(root.left)
       self.inOrderTraversal(root.right)
       print(root.data,end=" ")
       
       
    
if __name__=='__main__':
   tree=TreeNode()
   while True:
       data=int(input("Enter data "))
       if data>0:
           tree.append(data)
       else:
           break
   tree.inOrderTraversal(tree.root)
#    tree.preOrderTraversal(tree.root)
#    tree.postOrderTraversal(tree.root)
   
