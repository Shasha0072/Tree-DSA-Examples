class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#                 1
#              /     \
#             2       6
#            / \       \
#           3   5       7
#                \     /
#                 10  8
node1 = Node(1)
node1.left = Node(2)
node1.right = Node(6)
node1.left.left = Node(3)
node1.left.right = Node(5)
node1.left.right.right = Node(10)
node1.right.right = Node(7)
node1.right.right.left = Node(8)

def inorder(root):
    l = []
    inorderHelper(root, l)
    return l
def inorderHelper(root, l):
    if root == None:
        return 0

    inorderHelper(root.left, l)
    l.append(root.data)
    inorderHelper(root.right, l)
    return

def invertBinaryTree(tree):

    if tree == None:
        return
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    tree.left, tree.right = tree.right, tree.left
    return

print(inorder(node1))
invertBinaryTree(node1)
print(inorder(node1))
