# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        path=0
        stack=[]
        while root or stack:
            while root:
                path+=root.val
                stack.append((root,path))
                root=root.left
            root,path=stack.pop()
            if not root.right and not root.left and path==targetSum:
                return True
            root=root.right
        return False
#上面这个方法不太好，还要每次判断是否有root.right和root.left
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return True if root.val==targetSum else False
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)
#上面这个方法亦有缺点，思路简单，暴力DFS
from collections import deque
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # 队列里存：(当前节点, 截止到该节点的总和)
        queue = deque([(root, root.val)])
        
        while queue:
            node, curr_sum = queue.popleft()
            
            # 如果是叶子节点且和相等，直接通关
            if not node.left and not node.right and curr_sum == targetSum:
                return True
            
            # 分别把左右儿子和累加后的值入队
            if node.left:
                queue.append((node.left, curr_sum + node.left.val))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val))
        
        return False
#上面这个方法是BFS的解法