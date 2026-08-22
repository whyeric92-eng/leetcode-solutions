# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=0
        stack=[]
        path=""
        while root or stack:
            while root:
                path+=str(root.val)
                stack.append((root,path))
                root=root.left
            root,path=stack.pop()
            if not root.left and not root.right:
                res+=int(path)
            root=root.right
        return res
#也可以递归
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_sum):
            # 基准条件：如果节点为空，返回 0
            if not node:
                return 0
            
            # 计算当前路径的数字值（父级数字 * 10 + 当前节点值）
            current_sum = current_sum * 10 + node.val
            
            # 如果到达叶子节点，说明找到了一条完整路径，直接返回它的值
            if not node.left and not node.right:
                return current_sum
            
            # 如果不是叶子节点，就继续递归左右子树，并将两边的结果相加
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # 从根节点开始递归，初始路径和为 0
        return dfs(root, 0)