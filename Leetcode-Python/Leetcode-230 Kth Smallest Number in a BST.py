# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None
        # 这种self.写法不止出现在__init__里面 这样同样可以 本质就是实例属性
        # 在这种多层递归的写法中特别常见 因为这样可以避免每次都把某个变量传入函数当中
        def dfs(node):
            if self.result is not None:
                return 
            # 这个地方很关键 找到 self.result之后 就直接return
            if node.left:
                dfs(node.left)
            self.count+=1
            if self.count == k:
                self.result = node.val
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.result
#这道题的思路不用想的特别复杂 最简单的方式无非就是拿Recursion遍历一遍 存在list当中 直接取index 但是这样就是无法提前退出