

class Node :

    __slots__ = '_element', '_next'


    def __init__(self, element  , next):

        self._element = element
        self._next = next

    


if __name__ == "__main__":

    n1 = Node(7,None)
    n2 = Node(8,None)

    print(n1._element)
