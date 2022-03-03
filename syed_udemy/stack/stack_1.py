class StacksArray:
    def __init__(self):
        self.data = []

    def isEmpty(self):

        return len(self.data) == 0

    def push(self,e):
        self.data.append(e)

    def poped(self):

        if self.isEmpty():
            print("stack is empty")
            return
        else :
            self.data.pop()


if __name__ == "__main__":

     A = StacksArray()
     A.push(1)
     A.push(2)
     A.push(3)

     print(A.data)
     print(A.poped())
     print(A.data)