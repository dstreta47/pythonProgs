from collections import defaultdict, deque

def knighttour(x,y):
    cor = [(1, 2), (2, 1), (2, -1), (1, -2),(-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    def bfs(x,y):
        visited = set()
        queue = deque([(0,0)])
        steps = 0
        while queue:
            level = len(queue)
            for i in range(level):
                c_x,c_y = queue.popleft()

                if (c_x,c_y) == (x,y):
                    return steps

                for o_x,o_y in cor:
                     n_x,n_y = c_x + o_x , c_y + o_y
                     if(n_x,n_y) not in visited:
                         visited.add((n_x,n_y))
                         queue.append((c_x,c_y))

                steps +=1  
        return bfs(x,y)

print(knighttour(3,2))                          
