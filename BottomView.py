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



class Solution:
    def bottomView(self, root):
        dic = {}
        self.bottomViewHelper(root, 0, 0, dic)
        print(dic)
        res = []
        for key, value in dic.items():
            if len(value) == 1:
                res.append(value[0][-1])
            else:
                maxhLevel = 0
                bottomNode = value[0][-1]
                for i in value:
                    if i[0] > maxhLevel:
                        maxhLevel = i[0]
                        bottomNode = i[1]
                res.append(bottomNode)
        return res

        # code here

    def bottomViewHelper(self, root, vLevel, hLevel, dic):
        if root == None:
            return

        self.bottomViewHelper(root.left, vLevel - 1, hLevel + 1, dic)
        if vLevel not in dic:
            dic[vLevel] = [[hLevel, root.data]]
        else:
            dic[vLevel].append([hLevel, root.data])
        self.bottomViewHelper(root.right, vLevel + 1, hLevel + 1, dic)

        return


sol = Solution()
res = sol.bottomView(node1)
print(res)