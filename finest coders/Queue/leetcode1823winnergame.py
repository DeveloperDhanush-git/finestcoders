from collections import deque
class winnergame:
    def winner(self,n,k):
        queue = deque()
        for i in range(1,n+1):
            queue.append(i)
        while len(queue)!=1:
            for i in range(1,k+1):
                d = queue.popleft()
                if i!=k:
                    queue.append(d)
            queue.popleft()
        return queue[0]
list = winnergame()
n = int(input())
k = int(input())
print(list.winner(n,k))