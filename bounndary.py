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


def printBoundaryView(root):
     l = []
     getleftboundary(root, l)
     getleafnodes(root, l)
     getrightboundary(root, l)
     return l

def getleftboundary(root, l):
    if root == None:
        return
    if root.left:
        getleftboundary(root.left, l)
    if root.data not in l:
        l.append(root.data)
        return
    return

def getrightboundary(root, l):
    if root == None:
        return
    if root.right:
        getrightboundary(root.right, l)
    if root.data not in l:
        l.append(root.data)
        return
    return

def getleafnodes(root, l):
    if root == None:
        return
    if root.left == None and root.right == None:
        if root.data not in l:
            l.append(root.data)
            return
        return
    getleafnodes(root.left,l)
    getleafnodes(root.right, l)
    return

print(printBoundaryView(node1))