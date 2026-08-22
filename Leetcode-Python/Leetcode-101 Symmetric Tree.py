# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val==right.val:
                return isMirror(left.left,right.right) and isMirror(left.right,right.left)
            else:
                return False
        return isMirror(root.left,root.right)
    
#iterative
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
            
        queue = deque([(root.left, root.right)])
        
        while queue:
            node1, node2 = queue.popleft()
            
            # 都为空，继续判断队列中的其他节点
            if not node1 and not node2:
                continue
            
            # 只有一个为空，或者值不相等，说明不对称
            if not node1 or not node2 or node1.val != node2.val:
                return False
                
            # 将需要比较的节点成对入队
            # 1. 左节点的左孩子 vs 右节点的右孩子 (外侧)
            queue.append((node1.left, node2.right))
            # 2. 左节点的右孩子 vs 右节点的左孩子 (内侧)
            queue.append((node1.right, node2.left))
            
        return True