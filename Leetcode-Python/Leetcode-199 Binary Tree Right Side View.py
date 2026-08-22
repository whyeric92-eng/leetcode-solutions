# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue,res=[],[]
        queue.append((root,0))
        pre_height,pre_node=None,None
        while queue:
            temp,height=queue.pop(0)
            if pre_height is not None and pre_node and height>pre_height:
            #这个地方有个大坑 不能写if pre_height (问题是pre_height=0的时候会自动算为false)
                res.append(pre_node.val)
            pre_node,pre_height=temp,height
            if temp.left:
                queue.append((temp.left,height+1))
            if temp.right:
                queue.append((temp.right,height+1))
        res.append(temp.val)
        return res

#标准O(N)版本
#同时这个不需要手动维护height 当前queue的长度即是这一层个数
from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()  # O(1)
                if i == level_size - 1:  # 每层最后一个即为右视图
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res