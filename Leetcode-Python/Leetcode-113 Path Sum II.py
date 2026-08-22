# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res=[]
        stack=[]
        path=[]
        cur=0
        if not root:
            return []
        while stack or root:
            while root:
                cur+=root.val
                path.append(root.val)
                stack.append((root,path[:],cur))
                #传path[:]不要传path
                root=root.left
            root,path[:],cur=stack.pop()
            if not root.left and not root.right and cur==targetSum:
                res.append(path[:])
            root=root.right
        return res