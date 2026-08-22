# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res=True
        if not root:
            return True
        if root.left:
            le=root.left
            while le.right and le.val<root.val:
                le=le.right
            if le.right or le.val>=root.val:
                return False
            res*=self.isValidBST(root.left)
        if root.right:
            ri=root.right
            while ri.left and ri.val>root.val:
                ri=ri.left
            if ri.left or ri.val<=root.val:
                return False
            res*=self.isValidBST(root.right)
        return True if res==1 else False