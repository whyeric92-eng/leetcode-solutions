from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left_level,right_level=0,0
        if not root:
            return 0
        cur,cur1=root,root
        while cur:
            left_level+=1
            cur=cur.left
        while cur1:
            right_level+=1
            cur1=cur1.right
        if left_level==right_level:
            return 2**left_level-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
#时间复杂度是 O((log n)²)，比 O(n) 快很多
#高度为h(log n) 大致为h的平方
#递归层数 * 每层工作量 (h的平方)