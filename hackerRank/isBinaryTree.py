def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BST():

    def __init__(self):
        self.root = None

    def insert(self,data):

        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else :
            current = self.root
            while True:
                if data == current.data:
                    return

                if data < current.data:
                    if not current.left:
                        current.left = new_node
                        return
                    else:
                        current = current.left
                elif data > current.data:
                    if not current.right:
                        current.right = new_node
                        return
                    else :
                        current = current.right


def isBst(root):
    pass



if __name__  == "__main__":

    bst1 = BST()
    bst1.insert(1)
    bst1.insert(2)
    bst1.insert(3)
    bst1.insert(0)
    inOrder(bst1.root)

    print(isbst(bst1.root))