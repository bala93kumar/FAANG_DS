import heapq

class Edge :

    def __init__(self, weight, strt_ver, end_ver):
        self.weight = weight
        self.strt_ver = strt_ver
        self.end_ver = end_ver

class Vertex :
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.preceding = None
        self.adj_list = []
        self.min_dis = float('inf')

    def __lt__(self,other):
        return self.min_dis < other.min_dis

    def printGraph(self):
        length = len(self.adj_list)
        print(length)

class DijkstraAlgo:

    def __init__(self):
        self.list_1 = []

    def calculate(self,strt_ver):
        pass




if __name__ == "__main__":

    #create the vertices
    node1 = Vertex("A")
    node2 = Vertex("B")
    node3 = Vertex("C")
    node4 = Vertex("D")
    node5 = Vertex("E")
    node6 = Vertex("F")
    node7 = Vertex("G")
    node8 = Vertex("H")

    #create Edges

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node6)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    #handle the neighbours

    node1.adj_list.append(edge1)
    node1.adj_list.append(edge2)
    node1.adj_list.append(edge3)
    node2.adj_list.append(edge4)
    node2.adj_list.append(edge5)
    node2.adj_list.append(edge6)
    node8.adj_list.append(edge7)
    node8.adj_list.append(edge8)
    node5.adj_list.append(edge9)
    node5.adj_list.append(edge10)
    node5.adj_list.append(edge11)
    node6.adj_list.append(edge12)
    node6.adj_list.append(edge13)
    node3.adj_list.append(edge14)
    node3.adj_list.append(edge15)
    node4.adj_list.append(edge16)

    # print(node1.adj_list.__dict__.values())

    print(node1.printGraph())

    #can't understand







