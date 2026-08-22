# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index=-1
        def inorder(root):
            if not root:
                return []
            return inorder(root.left)+[root.val]+inorder(root.right)
        self.nodes=inorder(root)

    def next(self) -> int:
        self.index+=1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        return self.index+2<=len(self.nodes)
#缺点是这个的空间复杂度太高 因为存储了所有node

#迭代器就是一种“只记录当前位置，并能随时推算出下一步”的数据读取工具
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left

    def next(self) -> int:
        node=self.stack.pop()
        if node.right:
            temp=node.right
            while temp:
                self.stack.append(temp)
                temp=temp.left
        return node.val
#先压node开始的所有左子树 pop出某个节点 该节点如果有右子树 进行同样的操作

    def hasNext(self) -> bool:
        return self.stack!=[]
#标准的O(h)的空间复杂度的解法
#Stack 模拟递归的模板（即 __init__ 中先压栈，next() 中处理右子树并再次压栈）
#以后遇到中序遍历、前序遍历相关的题目，都可以套用这个栈的操作
#只需要一个attribute即可 因为stack的最后一个就是next 不用index来维护

#关于这类design的题目 定义哪些attribute是最重要的点
#可以尝试思考:
# 1.为了完成这些function 我需要知道哪些信息
# 2.为了记录这些信息 我需要准备哪些数据结构