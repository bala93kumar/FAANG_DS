
from collections import deque

def isValid(x,y,grid,visited):
    if (  (x>=0 and y >=0)  and (x < len(grid) and y <len(grid)) and (x,y) not in visited  ):
        return True
    return False


def minDistance(graph,m,n):
    visited = set()
    q = deque()

    source_row = 0
    source_col = 0

    dest_row = 0
    dest_col = 0

    for i in range(0,m):
        for j in range(0,n):
            if graph[i][j] == 's':
                source_row = i
                source_col = j
                q.append(((i,j),0))
                visited.add((i,j))

    while len(q):

        source, distance = q.pop()
        source_x, source_y = source

        if grid[source_x][source_y] == 'd':
            return distance

        # print(f" {source_x} : {source_y}  ".format(source_x, source_y)  )
        # print(distance)
        # print(source_distance)
        # move up
        if isValid(source_x-1, source_y,grid,visited):
            q.append(((source_x-1,source_y),distance+1))
            visited.add((source_x-1, source_y))
        #move down
        if isValid(source_x+1, source_y,grid,visited):
            q.append(((source_x+1,source_y),distance+1))
            visited.add((source_x+1, source_y))
        #move left
        if isValid(source_x, source_y-1, grid, visited):
            q.append(((source_x , source_y-1), distance + 1))
            visited.add((source_x , source_y-1))
        #move right

        if isValid(source_x, source_y + 1, grid, visited):
            q.append(((source_x, source_y+1), distance + 1))
            visited.add((source_x, source_y + 1))

    return -1








if __name__ == '__main__':
    grid = [['0', '*', '0', 's'],
            ['*', '0', '*', '*'],
            ['0', '*', '*', '*'],
            ['d', '*', '*', '*']]

    m = len(grid)
    n = len(grid[0])


    print(minDistance(grid,m,n))