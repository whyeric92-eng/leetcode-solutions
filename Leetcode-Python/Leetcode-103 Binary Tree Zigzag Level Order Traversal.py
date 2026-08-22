# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res=[]
        queue=[]
        temp=root
        level=0
        if temp is not None:
            queue.append((temp,level))
            while queue:
                temp,level=queue.pop(0)
                if len(res)==level:
                    res.append([])
                if level%2==0:
                    res[level].insert(0,temp.val)
                else:
                    res[level].append(temp.val)
                if temp.right:
                    queue.append((temp.right,level+1))
                if temp.left:
                    queue.append((temp.left,level+1))
        return res