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
    def deleteSingleChild(self):
        queue=deque()
        queue.append([self.root,None])
        while queue:
            curr,parent=queue.popleft()
            if (curr.left and curr.right==None) or (curr.right and curr.left==None):
                if curr.left:
                    child=curr.left
                else:
                    child=curr.right
            if parent==None:
                    self.root=child
            else:
                if curr==parent.left:
                    parent.left=child
                else:
                    parent.right=child
        if curr.left:
            queue.append([curr.left,curr])
        if curr.right:
            queue.append([curr.right,curr])

    
if __name__ == "__main__":
    tree = TreeNode()
    while True:
        data = int(input())
        if data >=0:
            tree.append(data)
        else:
            break
    tree.deleteSingleChild()
           