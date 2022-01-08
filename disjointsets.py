class disjointset:
    def __init__(self,n):
        self.u = list(range(n))

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: 
            self.u[ra] = rb
    
    def find(self, a):
        while self.u[a] != a: 
            a = self.u[a]
        return a

    def connected(self,x,y):
        return self.find(x) == self.find(y)


    def provinces(self,isConnected):
        if not isConnected:
            return 0

        s = len(isConnected)    
        uf = disjointset(s)
        for r in range(s):
            for c in range(r,s):
                if   isConnected[r][c] ==1:
                    uf.union(r,c)

        return len(set([uf.find(i) for i in range(s)]))              
    

# vertices = ["A","B","C","D","E"]
isConnected = [[1,1,0],[1,1,0],[0,0,1]]

ds = disjointset(len(isConnected))
# ds.union("A","B")
# ds.union("B","C")
# ds.union("C","D")
# print(ds.find("D"))
# print(ds.connected("A", "B"))
print(ds.provinces(isConnected))
#print(list(range(5)))








