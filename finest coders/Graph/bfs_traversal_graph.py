from collections import defaultdict,deque
class graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    def add_edge(self,src,dest):
        self.adj_list[src].append(dest)
        
    # def bfs(self,src):
    #     visited = set()
    #     queue = deque()
    #     queue.append(src)
    #     visited.add(src)
    #     while queue:
    #         src = queue.popleft()
    #         for dest in self.adj_list[src] :
    #             if dest not in visited:
    #                 visited.add(dest)
    #                 queue.append(dest)
    #     for node in visited:
    #         print(node,end=" ")
    def dfs(self,src,visited=None):
        if visited is None:
            visited = set()
        visited.add(src)
        print(src,end=" ")
        for dest in self.adj_list[src]:
            if dest not in visited:
                self.dfs(dest,visited)
                
    # def displaygraph(self):
    #     for src,dest,weight in sorted(self.adj_list.items()):
    #         print(src,"->",dest)
        
if __name__ == '__main__':
    g = graph()
    while True:
        src,dest = map(int,input().split())
        if src >= 0 and dest>=0:
            g.add_edge(src,dest)
        else:
            break
    src = int(input())
    # g.bfs(src)
    g.dfs(src)
        
    