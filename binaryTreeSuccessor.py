class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right is not None:
	    return getLeftmostChild(node.right)

    return getRightmostParent(node)

def getLeftmostChild(node):
    currentNode= node
    while currentNode.left is not None:
        currentNode= currentNode.left

    return currentNode.value

def getRightmostParent(node):
    currentNode= node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode= currentNode.parent
    return currentNode.parent.value

myTree= BinaryTree(45)
myTree.left= BinaryTree(25)
myTree.right= BinaryTree(55)
myTree.left.left= BinaryTree(15)
myTree.left.right= BinaryTree(26)
myTree.right.left= BinaryTree(53)
myTree.right.right= BinaryTree(56)  

p= findSuccessor(myTree, myTree.right)
print(p)

# print(type(myTree.right))
