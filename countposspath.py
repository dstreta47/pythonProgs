class Graph:
    def __init__(self,V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self,u,v):
        self.adj[u].append(v)

    def countPaths(self,s,d):
        visited = [False] * self.V
        pathcount = [0]
        self.countpathutil(s,d,visited,pathcount)
        return pathcount[0]

    def countpathutil(self,u,d,visited,pathcount):
        visited[u] = True
        if(u==d):
            pathcount[0] +=1
        else:
            i=0
            while i< len(self.adj[u]):
                if(not visited[self.adj[u][i]]):
                    self.countpathutil(self.adj[u][i],d,visited,pathcount)
                i+=1

        visited[u] = False             


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s=2
d=3

print(g.countPaths(s,d))
