
from collections import defaultdict


def dfs(grid:list[list[int]],row,col):
    num = 1
    grid[row][col] = 0
    lst = [(row,col+1), (row,col-1),(row+1,col),(row-1,col)]
    for row,col in lst:
        if row >= 0 and col >=0 and row <len(grid) and col< len(grid[0]) and grid[row][col] == 1:
            num += dfs(grid,row,col)
    return num




def maxAreaOfIsland(grid:list[list[int]]):
    area_island =0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                area_island = max(area_island,dfs(grid,r,c) )
    return area_island


if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

    print(maxAreaOfIsland(graph))