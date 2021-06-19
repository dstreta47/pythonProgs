class BinaryTree:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

node= BinaryTree(10)
node.left= BinaryTree(20)
node.right= BinaryTree(30)
node.left.left= BinaryTree(15)
node.left.right= BinaryTree(21)
node.right.left= BinaryTree(26)
node.right.right= BinaryTree(33)

def bstInvert(root):
    if root is None:
        return 
    swapleftright(root)
    bstInvert(root.left)
    bstInvert(root.right)

def swapleftright(root):
    root.left, root.right= root.right, root.left

p= bstInvert(node)
print(node.left.data, node.right.data)
