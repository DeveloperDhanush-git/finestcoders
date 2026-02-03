from collections import deque
class Node:
    def __init__(self,data):
        self.data = data     
        self.right = None
        self.left = None
class TreeNode:
    def __init__(self):
        self.root = None
    def append(self,data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is not None:
                        temp = temp.left
                    else:
                        temp.left = newnode
                        break
                else:
                    if temp.right is not None:
                        temp = temp.right
                    else:
                        temp.right = newnode
                        break
                    
    def bfs(self,n1,n2,root):
        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            temp = queue.popleft()
            if temp.data == n1 or temp.data==n2:
                count+=1
            if temp.left != None:
                queue.append(temp.left)
            if temp.right!= None:
                queue.append(temp.right)
                
    def leastCommonAncester(self,n1,n2):
        count = self.bfs(n1,n2)
        if count!=2:
            return -1
        temp = self.root
        if temp == None:
            return -1
        while temp:
            if n1<temp.data and n2<temp.data:
                temp = temp.left
            elif n1>temp.data and n2>temp.data:
                temp = temp.right
            elif n1<temp.data and n2>temp.data or n1>temp.data and n2<temp.data:
                print("Ansester of n1 and n2 :")
                return temp.data
            else:
                return -1         
            
if __name__=='__main__':
   tree=TreeNode()
   while True:
       data=int(input("Enter data "))
       if data>0:
           tree.append(data)
       else:
           break
   n1 = int(input())
   n2 = int(input())
   print(tree.leastCommonAncester(n1,n2))