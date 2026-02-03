from collections import defaultdict
class graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    def add_edge(self,src,dest,weight):
        self.adj_list[src].append([(dest,weight)]) #for directed graph
        
        # self.adj_list[dest].append(src) #for undirected graph
 
    def displaygraph(self):
        for src,dest,weight in sorted(self.adj_list.items()):
            print(src,"->",(dest,weight))
        
if __name__ == '__main__':
    g = graph()
    while True:
        src,dest,weight = map(int,input().split())
        if src >= 0 and dest>=0 and weight>=0:
            g.add_edge(src,dest,weight)
        else:
            break
    g.displaygraph()
        
    