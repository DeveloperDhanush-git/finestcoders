from collections import deque

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

    def bfs(self, root):
        queue = deque()
        queue.append(root)
        while queue:
            temp = queue.popleft()
            print(temp.data, end=" ")
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
        print()

    def findLCA(self, root, n1, n2):
        while root:
            if n1 < root.data and n2 < root.data:
                root = root.left
            elif n1 > root.data and n2 > root.data:
                root = root.right
            else:
                return root
        return None

    def findDistanceFromNode(self, root, n):
        distance = 0
        while root:
            if n < root.data:
                root = root.left
            elif n > root.data:
                root = root.right
            else:
                return distance
            distance += 1
        return -1

    def distanceBetweenNodes(self, n1, n2):
        lca = self.findLCA(self.root, n1, n2)
        if not lca:
            return -1
        d1 = self.findDistanceFromNode(lca, n1)
        d2 = self.findDistanceFromNode(lca, n2)
        return d1 + d2


if __name__ == '__main__':
    tree = TreeNode()
    while True:
        data = int(input("Enter data: "))
        if data > 0:
            tree.append(data)
        else:
            break

    print("\nBFS Traversal:")
    tree.bfs(tree.root)

    n1 = int(input("\nEnter first node value: "))
    n2 = int(input("Enter second node value: "))
    dist = tree.distanceBetweenNodes(n1, n2)
    print(f"Distance between {n1} and {n2}:", dist)
