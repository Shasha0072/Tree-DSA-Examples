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

# def height(root):
#     if root == None:
#         return 0
#     return 1 + max(height(root.left), height(root.right))
# def diameter(root):
#     if root == None:
#         return 0
#     lheight = height(root.left)
#     rheight = height(root.right)
#     ldiameter = diameter(root.left)
#
#
#     rdiameter = diameter(root.right)
#
#     return max(max(ldiameter, rdiameter), lheight + rheight + 1)
# print(diameter(node1))

class Height:
    def __init__(self):
        self.h = 0

def diameter(root):
    height = Height()
    return helper(root, height)
def helper(root, height):

    lh = Height()
    rh = Height()

    if root == None:
        height.h = 0
        return 0
    ld = helper(root.left, lh)
    rd = helper(root.right, rh)
    height.h = max(lh.h, rh.h) + 1

    return max(lh.h + rh.h +1, max(ld, rd))
print(diameter(node1))