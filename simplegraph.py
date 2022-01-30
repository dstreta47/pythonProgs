
from collections import defaultdict

class Graph:
    def __init__(self,no):
        self.graph = defaultdict(list)
        self.no = no

    def add_edge(self,src,dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)


g = Graph(5)
g.add_edge("A","B")
g.add_edge("B","C")
g.add_edge("C","D")
g.add_edge("D","A")

print(list(g.graph))





