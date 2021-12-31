def issafe(mat,visited,x,y):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and not (mat[x][y] == 0 or visited[x][y])    

def findLongestPath(mat,visited,i,j,dest, max_dist =0, dist = 0):
    if mat[i][j] ==0:
        return 0

    if(i,j) == dest:
        return max(dist,max_dist)
    visited[i][j] = 1
    if issafe(mat,visited,i+1,j):  #bottom
        max_dist = findLongestPath(mat,visited,i+1,j,dest,max_dist,dist+1)

    if issafe(mat,visited,i,j+1):  #right
        max_dist = findLongestPath(mat,visited,i,j+1,dest,max_dist,dist+1)
    if issafe(mat,visited,i-1,j):  #top
        max_dist = findLongestPath(mat,visited,i-1,j,dest,max_dist,dist+1)
    if issafe(mat,visited,i,j-1):  #left
        max_dist = findLongestPath(mat,visited,i,j-1,dest,max_dist,dist+1)
    visited[i][j]=0
    return max_dist    


#wrapper
def findLongestPathLength(mat,src,dest):
    i,j = src
    x,y = dest
    #base case
    if not mat or len(mat) == 0 or mat[i][j] ==0 or mat[x][y] == 0:
        return 0
    (m,n) = (len(mat),len(mat[0]))
    visited = [[0 for x in range(n)] for y in range(m)]
    return findLongestPath(mat,visited,i,j,dest)


mat = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]]

src = (0,0)
dest = (5,7)
print("the maximum path is ", findLongestPathLength(mat,src,dest))        
