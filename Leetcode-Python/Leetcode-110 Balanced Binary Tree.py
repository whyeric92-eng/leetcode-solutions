# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right))+1        
        def check(root):
            if not root:
                return True
            if abs(height(root.left)-height(root.right))<=1:
                return True
            return False
        stack=[]
        if not root: return True
        stack.append(root)
        while stack:
            temp=stack.pop()
            if check(temp):
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
            else:
                return False
        return True
class Solution(object):
    def isBalanced(self, root):
        def get_height(node):
            if not node:
                return 0
            
            left = get_height(node.left)
            if left == -1: return -1  # 左子树已经不平衡了，直接剪枝
            
            right = get_height(node.right)
            if right == -1: return -1 # 右子树已经不平衡了
            
            # 如果左右高度差大于 1，返回 -1 表示不平衡
            if abs(left - right) > 1:
                return -1
            
            # 否则返回真实高度
            return max(left, right) + 1

        return get_height(root) != -1