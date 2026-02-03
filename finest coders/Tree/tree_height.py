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
                    
    def treeheight(self,root):
        if root == None:
            return 0
        lheight = self.treeheight(root.left)
        rheight = self.treeheight(root.right)
        return max(lheight,rheight)+1
        
if __name__ == '__main__':
    tree = TreeNode()
    while True:
        try:
            data = int(input("Enter data (negative to stop): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if data > 0:
            tree.append(data)
        else:
            break

    print(tree.treeheight(tree.root))
