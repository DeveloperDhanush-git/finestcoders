from queue import PriorityQueue
from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    def addEdge(self, src, dest,weight):
        self.adj_list[src].append((dest,weight))
    def displaygraph(self):
        for src,dest,weight in sorted(self.adj_list.items()):
            print(src,"->",(dest,weight))