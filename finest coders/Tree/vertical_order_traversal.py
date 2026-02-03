from collections import defaultdict, deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self):
        self.root = None

    def append(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is not None:
                        temp = temp.left
                    else:
                        temp.left = newNode
                        break
                else:
                    if temp.right is not None:
                        temp = temp.right
                    else:
                        temp.right = newNode
                        break

    def verticalorder(self):
        queue = deque()
        result = defaultdict(list)
        queue.append([self.root,0])
        while queue:
            curr , hd = queue.popleft()
            if curr.left!=None:
                queue.append((curr.left,hd-1))
            if curr.right!=None:
                queue.append((curr.right,hd+1))
            result[hd].append(curr.data)
            
        for hd,node in sorted(result.items()):
            print(hd,"->",node)
                
if __name__ == '__main__':
    tree = TreeNode()
    while True:
        data = int(input("Enter data: "))
        if data > 0:
            tree.append(data)
        else:
            break
    tree.verticalorder()
