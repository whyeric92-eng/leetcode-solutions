# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        temp = root.val
        res = []
        if left:
            res.extend([f"{temp}->" + cur for cur in left])
        if right:
            res.extend([f"{temp}->" + cur for cur in right])
        if not right and not left:
            res.append(f"{temp}")
        return res