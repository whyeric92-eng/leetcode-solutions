# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue=[]
        res=[]
        level=0
        cur=root
        if root is not None:
            queue.append((root,0))
            while queue:
                temp,level=queue.pop(0)
                if len(res)==level:
                    res.append([])
                res[level].append(temp.val)
                if temp.left:
                    queue.append((temp.left,level+1))
                if temp.right:
                    queue.append((temp.right,level+1))
        return res[::-1]