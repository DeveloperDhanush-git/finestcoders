from collections import defaultdict,deque
class graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    def add_edge(self,src,dest):
        self.adj_list[src].append(dest)
        
    def dfs(self,src,visited=None):
        if visited is None:
            visited = set()
        visited.add(src)
        print(src,end=" ")
        for dest in self.adj_list[src]:
            if dest not in visited:
                self.dfs(dest,visited)
                
        
if __name__ == '__main__':
    g = graph()
    while True:
        src,dest = map(int,input().split())
        if src >= 0 and dest>=0:
            g.add_edge(src,dest)
        else:
            break
    src = int(input())
    g.dfs(src)
        
    