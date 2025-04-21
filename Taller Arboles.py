class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    @property
    def hasLeft(self):
        return self.left is not None
    
    @property
    def hasRight(self):
        return self.right is not None

    @property
    def left(self):
        return self.left
    
    @property
    def right(self):
        return self.right
    
    def setleft(self, left):
        self.left = left
        return self
    
    def setright(self,right):
        self.right = right
        return self

def printTree(tree):
    if tree.hasLeft:
        printTree(tree.left)
    if tree.hasRight:
        printTree(tree.right)
    print(tree.value)

    elemento1 = Node(1)
    elemento2 = Node(2)
    elemento3 = Node(3)
    elemento4 = Node(4)
    elemento5 = Node(5)

    elemento1.setleft(elemento2)
    elemento1.setright(elemento5)
    elemento2.setleft(elemento3)
    elemento2.setright(elemento4)

