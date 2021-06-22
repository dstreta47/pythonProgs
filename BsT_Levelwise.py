class BinaryTree:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

node= BinaryTree(10)
node.left= BinaryTree(9)
node.right= BinaryTree(11)
node.left.left= BinaryTree(8)
node.left.right= BinaryTree(12)
node.right.left= BinaryTree(13)
node.right.right= BinaryTree(15)


def levelWiseTraversal(tree):
    h= height(tree)

    for i in range(1,h+1):
        printCurrentLevel(tree, i)

def printCurrentLevel(tree, level):
    if tree is None:
        return 
    if level== 1:
        print(tree.data, end= " ")
    elif level>1:
        printCurrentLevel(tree.left, level-1)
        printCurrentLevel(tree.right, level-1)
        
def height(tree):
    if tree is None:
        return 0
    else:
        l_height= height(tree.left)
        r_height= height(tree.right)
        if l_height > r_height:
            return l_height +1
        else:
            return r_height +1

#        10
#       /  \  
#      9     11
#     / \    / \
#   8   12  13 15


p= levelWiseTraversal(node)
