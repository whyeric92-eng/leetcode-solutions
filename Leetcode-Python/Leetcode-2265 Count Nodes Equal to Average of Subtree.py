# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def sumOfNodes(root):
            if not root:
                return (0, 0)
            l_sum, l_num = sumOfNodes(root.left)
            r_sum, r_num = sumOfNodes(root.right)
            return (root.val + l_sum + r_sum, 1 + l_num + r_num)
        def judge(root):
            result = 0
            if not root:
                return 0
            res, num = sumOfNodes(root)
            if res//num == root.val:
                result += 1
            result += judge(root.left)
            result += judge(root.right)
            return result
        return judge(root)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def sumOfNodes(root):
            nonlocal count
            # 不能写global 应该用nonlocal
            if not root:
                return (0, 0)
            l_sum, l_num = sumOfNodes(root.left)
            r_sum, r_num = sumOfNodes(root.right)
            s = root.val + l_sum + r_sum
            n = 1 + l_num + r_num
            if s//n == root.val:
                count += 1
            return (s,n)
        sumOfNodes(root)
        return count