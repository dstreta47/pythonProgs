#               A
#              /  \ 
#           B       E
#          /
#        C
from collections import defaultdict, deque

class Graph:
    def __init__(self,no):
        self.graph = defaultdict(list)
        self.no = no

    def add_edge(self, src,dest):
        self.graph[src].append(dest)

    def bfs(self, s):
        visited = [s]
        queue = [s]
        while queue:
            s = queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)

    def noIsland(self,grid):
        no_of_island = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    queue.append((i,j))
                    self.bfs_grid(grid,queue)
                    no_of_island+=1
        return no_of_island           

    def bfs_grid(self,grid,queue):
        while queue:
            i,j = queue.popleft()
            for i,j in [i-1,j],[i+1,j],[i,j-1],[i,j+1]:
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1':
                    queue.append((i,j))
                    grid[i][j] =0



g = Graph(4)
# g.add_edge("A","B")
# g.add_edge("B","C")
# g.add_edge("A","E")
grid = [["1","1","0","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","1","1"]]

# g.bfs("A")
print(g.noIsland(grid))




