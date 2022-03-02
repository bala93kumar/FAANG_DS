class Node:

    __slots__ = '_element', '_next'

    def __init__(self , element , next):
        self._element = element
        self._next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def addLast(self, data):
        newNode  =  Node(data,None)
        if self.isempty():
            self.head = newNode
        else :
            self.tail._next  = newNode
        self.tail = newNode
        self.size += 1

    def insertFirst(self,data):
        newNode = Node(data,None)

        if self.isempty():
            self.head = newNode
            self.tail  = newNode
            self.size += 1
        else:

            newNode._next = self.head
            self.head = newNode
            self.size += 1

    def  display(self):

        counter = self.head

        while counter:

            print(counter._element, end='--->')
            counter  = counter._next

    def insertAny(self, data , position):

        newNode = Node(data,None)

        currentNode  = self.head
        count = 1

        if self.head :
            while count < position-1:
                currentNode = currentNode._next
                count += 1
        else :
            return -1

        nextto = currentNode._next
        currentNode._next =  newNode
        newNode._next = nextto

    def reverseLinkedList(self):


        if self.head == None :
            return None
        else :
            previous = None
            next = None

            node = self.head

            while node !=None:
                next = node._next
                node._next = previous
                previous = node

        return previous






    def searchElement(self, data):

        counter = self.head
        index = 0

        while counter:
            if counter._element == data:
                print(f'element is present at  {index} position')
                return
            else :
                counter = counter._next
                index +=1

        return "no element found"




if __name__ == "__main__":

    list1 = LinkedList()

    list1.addLast(1)
    list1.addLast(2)
    list1.addLast(3)

    list1.insertFirst(0)
    list1.display()

    print("after insert in position")

    list1.insertAny(8, 3)
    list1.display()

    list1.reverseLinkedList()

    list1.display()

    # list1.searchElement(2)







