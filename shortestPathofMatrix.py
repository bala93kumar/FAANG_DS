from collections import deque
def shortestPath(grid):

    m , n = len(grid), len(grid[0])
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

    if grid[0][0] !=0 or grid[m-1][n-1] !=0:
        return False
    q = deque()

    if grid[0][0] == 0:
        grid[0][0] = 1
        q.append((1,(0,0)))

    while q:
        steps , temp = q.popleft()
        r,c = temp[0], temp[1]
        if (r,c) == (m-1, n-1):
            return steps
        for i , j in dirs:
            new_r, new_c = r+i , c+j
            if  0<=new_r<m and 0<=new_c<n and grid[new_r][new_c] == 0 :
                q.append((steps+1,(new_r,new_c)))
                grid[new_r][new_c] = 1
    return -1


if __name__ == '__main__':
    grid = [[0,0,0],[1,1,0],[1,1,0]]

    print(shortestPath(grid))

