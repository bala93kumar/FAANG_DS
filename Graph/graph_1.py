import numpy as np


class Graph:

    def __init(self , vertices):
        self.vertices = vertices
        self.adjMat = np.zeros((vertices,vertices))

    def  insert_edge(self,u , v, x=1):
         self.adjMat[u][v]= x

    def remove_edge(self, u , v):
        self.adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self.adjMat[u][v] !=0

    def vertex_cout(self):

        return self.vertices

    def edge_count(self):
        edge_count = 0

        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMat[i][j] != 0:
                    edge_count += 1

        return edge_count

    def edges(self):




if __name__ == "__main__":




