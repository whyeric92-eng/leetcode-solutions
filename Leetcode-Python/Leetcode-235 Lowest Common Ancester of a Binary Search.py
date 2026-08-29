# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def judge(root,p,q):
            if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
                return root
            elif root.val > max(p.val, q.val):
                return judge(root.left,p,q)
            else:
                return judge(root.right,p,q)
        return judge(root,p,q)

#迭代
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
        return None