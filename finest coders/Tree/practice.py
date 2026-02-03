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
                    if temp.left!=None:
                        temp = temp.left
                    else:
                        temp.left = newnode
                        break
                else:
                    if temp.right!=None:
                        temp = temp.right
                    else:
                        temp.right = newnode
                        break
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
        
    def bfs(self,root):
        queue = deque()
        queue.append(root)   
        while queue:
            temp = queue.popleft()
            print(temp.data,end=" ")
            while queue:
                if temp.left!=None:
                    queue.append(temp.left)
                if temp.right!=None:
                    queue.append(temp.right)      
    
if __name__ == "__main__":
    tree = TreeNode()
    while True:
        data = int(input())
        if data >=0:
            tree.append(data)
        else:
            break
    tree.bfs(tree.root)
    tree.inorder(tree.root)
           