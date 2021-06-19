
class BinaryTree:
	def __init__(self, value, left=None, right= None):
		self.value= value
		self.left= left
		self.right= right

def binaryTreeDiameter(tree):
	return getTreeInfo(tree).diameter

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0)
	leftTreeInfo= getTreeInfo(tree.left)
	rightTreeInfo= getTreeInfo(tree.right)

	longesPathThroughRoot= leftTreeInfo.height+ rightTreeInfo.height
	maxDiameterSoFar= max(leftTreeInfo.diameter, rightTreeInfo.diameter)
	currentDiameter= max(longesPathThroughRoot, maxDiameterSoFar)
	currentHeight= 1+ max(leftTreeInfo.height, rightTreeInfo.height) #recursion allback add

	return TreeInfo(currentDiameter, currentHeight)




class TreeInfo:
	def __init__(self,diameter, height):
		self.diameter= diameter
		self.height= height
 
myTree= BinaryTree(10)
myTree.left= BinaryTree(9)
myTree.right= BinaryTree(11)
myTree.left.left= BinaryTree(8)
myTree.left.right= BinaryTree(20)
myTree.right.left= BinaryTree(6)
myTree.right.right= BinaryTree(12)

p= binaryTreeDiameter(myTree)
print(p)
