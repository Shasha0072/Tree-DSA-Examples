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
# node1.left.right.right = Node(10)
node1.right.right = Node(7)
node1.right.right.left = Node(8)

class Height:
    def __init__(self):
        self.h = 0
def isBalanced(root):
    height = Height()
    return isBalancedHelper(root, height)
def isBalancedHelper(root, height):
    lh = Height()
    rh = Height()

    if root == None:
        height.h = 0
        return True

    ls = isBalancedHelper(root.left, lh)
    rs = isBalancedHelper(root.right, rh)

    height.h = max(lh.h, rh.h) + 1

    if abs(lh.h - rh.h) <= 1:
        return ls and rs

    return False
print(isBalanced(node1))
