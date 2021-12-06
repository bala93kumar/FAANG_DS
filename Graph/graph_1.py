import numpy as np

class Graph:

    def __init__(self , vertices):
        self.vertices = vertices
        self.adjMat = np.zeros((vertices,vertices))

    def  insert_edge(self,u , v, x=1):
         self.adjMat[u][v]= x

    def remove_edge(self, u , v):
        self.adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self.adjMat[u][v] == 1

    def vertex_count(self):

        return self.vertices

    def edge_count(self):
        edge_count = 0

        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjMat[i][j] != 0:
                    edge_count += 1

        return edge_count

    def edges(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if  self.adjMat[i][j] != 0:
                    print(i, '---', j )

    def outdegree(self, v):
        count = 0
        for j in range(self.vertices):
            if self.adjMat[v][j] !=0:
                count = count + 1
        return count

    def indegree(self,v):
        count = 0
        for j in range(self.vertices):
            if self.adjMat[v][j] !=0:
                count = count + 1
        return count

    def display(self):
        print(self.adjMat)

if __name__ == "__main__":

    graph1 = Graph(4)
    graph1.display()

    print("vertices : ", graph1.vertex_count())
    print("edges : ", graph1.edge_count())

    graph1.insert_edge(0,1)
    graph1.insert_edge(0,2)
    graph1.insert_edge(1,0)
    graph1.insert_edge(1,2)
    graph1.insert_edge(2,1)
    graph1.insert_edge(2,0)
    graph1.insert_edge(2,3)
    graph1.insert_edge(3,2)

    graph1.display()

    graph1.edges()

    print(graph1.exist_edge(1,3))









