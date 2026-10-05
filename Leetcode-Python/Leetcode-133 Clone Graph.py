class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = {}
        def dfs(node):
            if node in cloned:
                return cloned[node]
            copy = Node(val = node.val)
            cloned[node] = copy 
            #一定要先在递归之前登记 不然容易死环
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
    #每个dfs的作用就是deep copy这个node 返回这个node的deep copy版本