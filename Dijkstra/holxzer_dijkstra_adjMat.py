import sys
class DijkstraAlgo:
    def __init__(self,adj_mat,strt):
        self.adj_mat = adj_mat
        self.strt = strt
        self.v = len(adj_mat)
        self.visit = [False for i in range(len(adj_mat))]
        self.distance = [float('inf') for j in range(len(adj_mat))]
        self.distance[strt] = 0

    def get_min_vertex(self):

        min_vertex_value =  sys.maxsize
        min_vertex_index = 0

        for i in range(self.v):
            if not self.visit[i] and self.distance[i] < min_vertex_value:
                min_vertex_value  = self.distance[i]
                min_vertex_index = i

        return min_vertex_index

    def calculate(self):





if __name__ == "__main__":

    m  = [[0,7,5,2,0,0] ,
          [7,0,0,0,3,0],
          [5,0,0,10,4,0],
          [2,0,10,0,0,2],
          [0,3,4,0,0,6],
          [0,8,0,2,6,0]
          ]


