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

    def inOrderTraversal(self, root):
        if root is None:
            return
        self.inOrderTraversal(root.left)
        print(root.data, end=" ")
        self.inOrderTraversal(root.right)

    def kthElement(self, root, k):
        stack = []
        temp = root
        count = 0
        
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            count += 1
            if count == k:
                return temp.data
            temp = temp.right

if __name__ == '__main__':
    tree = TreeNode()
    while True:
        data = int(input("Enter data: "))
        if data > 0:
            tree.append(data)
        else:
            break
    
    print("In-order Traversal:", end=" ")
    tree.inOrderTraversal(tree.root)
    print()

    k = int(input("Enter k: "))

    left_result = tree.kthElement(tree.root.left, k)
    right_result = tree.kthElement(tree.root.right, k)

    print(left_result)
    print(right_result)
