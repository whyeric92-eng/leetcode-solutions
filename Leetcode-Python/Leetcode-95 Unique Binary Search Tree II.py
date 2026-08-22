# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        dp=[[] for _ in range(n+1)]
        dp[0]=[None]
        dp[1]=[TreeNode(1)]
        def trans(node,k):
            if not node:
                return 
            newnode=TreeNode(node.val+k)
            newnode.left=trans(node.left,k)
            newnode.right=trans(node.right,k)
            return newnode
        #这个地方一定要新建一个newnode一直用node会让数据丢失
        for i in range(2,n+1):
            for j in range(i):
                for l_node in dp[j]:
                    for r_node in dp[i-j-1]:
                        root=TreeNode(j+1)
                        root.left=l_node
                        root.right=trans(r_node,j+1)
                        dp[i].append(root)
        return dp[n] 