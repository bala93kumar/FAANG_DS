

from collections import deque

def rottenOrange(grid):

    m = len(grid)
    n = len(grid[0])
    visited = set()
    q = deque()

    for i in range(0,m) :
        for j in range(0,n):
            if grid[i][j] == 2:
                q.append(((i,j),0))
                visited.add((i,j))

    print(q)
    time = 0
    while q:
        index,time = q.popleft()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        r , c = index[0],index[1]
        for i,j in dirs:
            new_r,new_c = r+i , c+j
            if 0<=new_r<m and 0<=new_c<n and grid[new_r][new_c] == 1 and (new_r,new_c) not in visited:
                q.append(( (new_r,new_c), time+1 ))
                visited.add((new_r,new_c))
                grid[new_r][new_c] =2

    for i in range(0,m):
        for j in range(0,n):
            if grid[i][j] == 1:
                return -1

    return time




if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]

    print(rottenOrange(grid))



