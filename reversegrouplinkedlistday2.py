class Node:
    def __init__(self, data):
        self.data = data
        self.add = None

class SinglyLinkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.add != None:
                temp = temp.add
            temp.add = newnode

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.add
        print()
    
    def reverse_k_group(self, k):
        if not self.head or k == 1:
            return
        
        dummy = Node(0)
        dummy.add = self.head
        prev_group = dummy

        while True:
            kth = prev_group
            count = 0
            while count < k and kth.add:
                kth = kth.add
                count += 1
            if count < k:
                break

            group_prev = prev_group.add
            curr = group_prev.add
            for _ in range(k - 1):
                temp = curr.add
                curr.add = prev_group.add
                prev_group.add = curr
                curr = temp
            group_prev.add = curr
            prev_group = group_prev

        self.head = dummy.add


if __name__ == "__main__":
    sll = SinglyLinkedlist()
    while True:
        data = int(input())
        if data >= 0:
            sll.append(data)
        else:
            break

    print("original list:")
    sll.display()

    k = int(input("enter k: "))
    sll.reverse_k_group(k)
    sll.display()
