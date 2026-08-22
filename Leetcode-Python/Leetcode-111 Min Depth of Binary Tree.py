# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        elif root.left:
            return self.minDepth(root.left)+1
        elif root.right:
            return self.minDepth(root.right)+1
        else:
            return 1
#一样的思路，但是对代码进行瘦身
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        # 如果左子树或右子树有一个为空，返回非空子树深度 + 1
        # 如果都不为空，返回较小深度 + 1
        if not root.left or not root.right:
            return left + right + 1
        
        return min(left, right) + 1
#用BFS解决
from collections import deque
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        # 队列中存储 (当前节点, 当前深度)
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # 核心逻辑：一旦遇到叶子节点（左右子节点都为空），直接返回当前深度
            if not node.left and not node.right:
                return depth
            
            # 将子节点加入队列，深度 + 1
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0