
import sys

from heapq import heapify, heappop , heappush


def dijkstra(graph , strt , end):

    inf = sys.maxsize

    node_data = {}

    for i in graph:
        node_data[i] = {'cost': inf,  'pred': []}

    node_data[strt]['cost'] = 0
    visited = []
    tmp = strt
    # print(node_data)

    for i in range(len(graph)-1):
        if tmp not in visited:
            visited.append(tmp)
            min_heap = []
            for j in graph[tmp]:
                if j not in visited:
                    cost = node_data[tmp]['cost'] + graph[tmp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[tmp]['pred'] + list(tmp)
                    heappush(min_heap,(node_data[j]['cost'],j))
        heapify(min_heap)
        tmp = min_heap[0][1]
    print("shortest distance :" + str(node_data[end]['cost']))
    print("shortest path :" + str(node_data[end]['pred'] + list(end)))


# https://www.youtube.com/watch?v=OrJ004Wid4o&ab_channel=ThinkXAcademy

if __name__ == "__main__":

    graph = {

        'a': {'b':2, 'c':4},
        'b': {'a':2, 'c':3, 'd':8},
        'c': {'a':4, 'b':3, 'e':5,  'd':2},
        'd': {'b':8, 'c':2, 'e':11, 'f':22},
        'e': {'c':5, 'd':11,'f':1},
        'f': {'d':22,'e': 1}
    }

    dijkstra(graph, 'a', 'd')

    # for j in graph['a']:
    #     print(graph['a'][j])




