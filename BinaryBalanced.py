class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,isBalanced,height):
        self.isBalanced= isBalanced
        self.height = height


def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(node):
    if node == None:
        return TreeInfo(True,-1)   

    leftSubtreeInfo =  getTreeInfo(node.left)         
    rightSubtreeInfo =  getTreeInfo(node.right)     

    isBalanced = leftSubtreeInfo.isBalanced and  rightSubtreeInfo.isBalanced and abs(leftSubtreeInfo.height
                            - rightSubtreeInfo.height) <=1

    height = max(leftSubtreeInfo.height,rightSubtreeInfo.height)  +1

    return TreeInfo(isBalanced,height)

myTree= BinaryTree(45)
myTree.left= BinaryTree(25)
myTree.right= BinaryTree(55)
myTree.left.left= BinaryTree(15)
myTree.left.right= BinaryTree(26)
myTree.right.left= BinaryTree(53)
myTree.right.right= BinaryTree(56)
myTree.right.right.left= BinaryTree(52)  
myTree.right.right.right= BinaryTree(57)
myTree.right.right.left.left= BinaryTree(51)
myTree.right.right.left.right= BinaryTree(58)



p=heightBalancedBinaryTree(myTree)
print(p)
