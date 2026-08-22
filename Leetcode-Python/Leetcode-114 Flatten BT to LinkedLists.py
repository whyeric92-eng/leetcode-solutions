# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack=[]
        stack.append(root)
        new=TreeNode(0)
        dum=new.right
        while stack:
            cur=stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            new.right=cur
            new.left=None
            new=cur
        return dum
#中规中矩的pre-order traversal
def flatten(self, root):
    curr = root
    while curr:
        if curr.left:
            # 找到左子树的最右节点
            pre = curr.left
            while pre.right:
                pre = pre.right
            
            # 关键：将原来的右子树接到左子树的最右边
            pre.right = curr.right
            # 将左子树换到右边
            curr.right = curr.left
            curr.left = None
        
        # 继续下一个节点
        curr = curr.right