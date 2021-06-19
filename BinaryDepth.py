#program to find the sum of the depth of a binary tree
class BinaryTree:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None


# def NodeDepth(root):
#     sumofDepth=0
#     stack= [{"node":root, "depth":0}]
#     while len(stack)> 0:
#         nodeInfo= stack.pop()
#         node, depth= nodeInfo["node"], nodeInfo["depth"]
#         if node is None:
#             continue
#         sumofDepth += depth
#         stack.append({"node":node.left, "depth:":depth +1})
#         stack.append({"node":node.right, "depth:":depth +1})
#     return sumofDepth

myTree= BinaryTree(10)
myTree.left= BinaryTree(9)
myTree.right= BinaryTree(11)
myTree.left.left= BinaryTree(8)
myTree.left.right= BinaryTree(20)
myTree.right.left= BinaryTree(6)
myTree.right.right= BinaryTree(12)
# print(myTree.data, myTree.left.data, myTree.right.data)

def NodeDepth(node, depth= 0):
    if node is None:
        return 0
    return depth+ NodeDepth(node.left, depth+1)+ NodeDepth(node.right, depth+1)

p= NodeDepth(myTree)
print(p)
