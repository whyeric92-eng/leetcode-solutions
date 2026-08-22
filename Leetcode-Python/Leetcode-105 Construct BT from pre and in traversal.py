# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        root=TreeNode(preorder[0])
        index=inorder.index(root.val)
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
class Solution(object):
    def buildTree(self, preorder, inorder):
        # 1. 预处理哈希表，提升查找速度
        in_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            # 2. 确定根节点
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 3. 获取根节点在中序遍历中的位置
            in_index = in_map[root_val]
            left_size = in_index - in_start
            
            # 4. 递归处理，仅传递索引（无切片）
            root.left = helper(pre_start + 1, pre_start + left_size, 
                               in_start, in_index - 1)
            root.right = helper(pre_start + left_size + 1, pre_end, 
                                in_index + 1, in_end)
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)