# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        cur = root
        stack = []
        
        # 记录前一个遍历到的节点
        pre = None 
        # 记录需要被交换的两个错误节点
        first = None
        second = None

        # 经典的中序遍历迭代写法
        while cur or stack:
            # 1. 一路向左，把左子节点全部压入栈
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # 2. 弹出栈顶元素进行处理
            cur = stack.pop()
            
            # 3. 核心逻辑：判断当前节点与前驱节点的值
            if pre and pre.val > cur.val:
                # 第一次遇到降序：记录第一个错误节点 pre，和潜在的第二个错误节点 cur
                if not first:
                    first = pre
                    second = cur
                # 第二次遇到降序：只需要更新第二个错误节点 cur
                else:
                    second = cur
            
            # 4. 更新 pre，并转向右子树
            pre = cur
            cur = cur.right
            
        # 遍历结束后，统一交换两个错误节点的值
        if first and second:
            # Python 的快捷交换语法
            first.val, second.val = second.val, first.val

#其实就是展现inorder(BST转成sorted list的方法)的过程然后pre和cur一前一后来遍历