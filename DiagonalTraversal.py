class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#                 1
#              /     \
#             2        6
#            / \      /  \
#           3   5   4     7
#                \       /
#                 10    8
node1 = Node(1)
node1.left = Node(2)
node1.right = Node(6)
node1.right.left = Node(4)
node1.left.left = Node(3)
node1.left.right = Node(5)
node1.left.right.right = Node(10)
node1.right.right = Node(7)
node1.right.right.left = Node(8)



def diagonalTraversal(root):
    dic = {}
    diagonal = 1
    diagonalTraversalHelper(root, diagonal, dic)
    l = []
    for key, value in dic.items():
        l += value
    return l


def diagonalTraversalHelper(root, diagonal, dic):
    if root == None:
        return
    if diagonal not in dic:
        dic[diagonal] = [root.data]
    else:
        dic[diagonal].append(root.data)

    diagonalTraversalHelper(root.left, diagonal + 1, dic)
    diagonalTraversalHelper(root.right, diagonal, dic)
    return

print(diagonalTraversal(node1))

