
from typing import Collection
import collections


def dfs(r, c, graph):
    graph[r][c] = 0
    lst = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]
    for row, col in lst:
        if row >= 0 and col > 0 and row < len(graph) and col < len(graph[0]) and graph[row][col] == 1:
            dfs(row, col, graph)


if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

    print(graph)

    row = len(graph)
    col = len(graph[0])
    island = 0
    for r in range(row):
        for c in range(col):
            if graph[r][c] == 1:
                dfs(r, c, graph)
                island += 1

    print(island)
