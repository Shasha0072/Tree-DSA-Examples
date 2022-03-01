class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


#                 1
#              /     \
#             2       6
#            / \       \
#           3   5       7
#                \     /
#                 10  8
node1 = Node(1)
node2 = Node(2)
node2.parent = node1
node3 = Node(3)
node3.parent = node2
node5 = Node(5)
node5.parent = node2
node6 = Node(6)
node6.parent = node1
node7 = Node(7)
node7.parent = node6
node8 = Node(8)
node8.parent = node7
node10 = Node(10)
node10.parent = node5




def findSuccessor(tree, node):
    l = []
    h(tree, node, True, l)
    print(l)


def h(tree, node, B, l):
    if tree == None:
        return
    k = node

    h(tree.left, k, True, l)

    if tree.data == node:
        if B:
            l.append(tree.parent)
            print(tree.parent)
        else:
            l.append(tree.parent.parent)
            print(tree.parent.parent)

    h(tree.right, k, False, l)

print(findSuccessor(node1, 10))