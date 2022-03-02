class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
node1 = Node(1)
node4 = Node(4)
node2 = Node(2)
node7 = Node(7)
node3 = Node(3)
node5 = Node(5)
node6 = Node(6)
node4.left = node2
node4.right = node7
node2.left = node1
node2.right= node3
node7.left = node5
node5.right = node6

def find(root, target):
    if root == None:
        return False
    if root.data == target:
        return True
    elif root.data > target:
        if find(root.left, target):
            return True
        else:
            return False
    else:
        if find(root.right, target):
            return True
        else:
            return False
# for i in range(0,9):
#     print(f"for {i} == {find(node4, i)}")

# def findmin(root):
#     if root == None:
#         return None
#     current = root
#     while current.left:
#         current = current.left
#     return current.data
#
#
def findmax(root):
    if root == None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.data
# print(findmin(node4))
# print(findmax(node4))

def findmin(root):
    if root == None:
        return None
    if root.left == None:
        return root.data
    else:
        return findmin(root.left)
print(findmin(node4))

def predecessor(node):
    if node == None:
        return None
    if node.left:
        return findmax(node.left)
    else:
        return None

print(predecessor(node3))
def successore(node: Node):
    if node == None:
        return None
    if node.right:
        return findmin(node.right)
    else:
        return None

print(successore(node5))