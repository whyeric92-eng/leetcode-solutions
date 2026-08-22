"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        stack=[(root,0)]
        prev,height_old=None,0
        while stack:
            cur,height=stack.pop(0)
            if height>height_old:
                prev.next=None
            elif prev:
                prev.next=cur
            if cur.left:
                stack.append((cur.left,height+1))
            if cur.right:
                stack.append((cur.right,height+1))
            prev,height_old=cur,height
        return root
    
from collections import deque

class Solution(object):
    def connect(self, root):
        if not root:
            return None
        
        # 使用 deque 保证 popleft() 是 O(1)
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                cur = queue.popleft()
                
                # 如果不是当前层的最后一个节点，连接到队列中的下一个
                if i < level_size - 1:
                    cur.next = queue[0]
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    
        return root