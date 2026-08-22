# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None
        temp1=head
        n=0
        while temp1:
            n+=1
            temp1=temp1.next
        if n==1:
            return TreeNode(head.val)
        temp2=head
        temp=head
        for _ in range(n//2):
            temp=temp2
            temp2=temp2.next
        root=TreeNode(temp2.val)
        temp3=temp2.next
        temp.next=None
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(temp3)
        return root
class Solution(object):
    def sortedListToBST(self, head):
        # 1. 计算总长度
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        # 记录当前处理到链表的哪个节点了
        self.head = head
        
        def convert(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # 【左】先递归构建左子树，此时并不访问 head
            left_child = convert(left, mid - 1)
            
            # 【根】构建当前根节点
            # 此时递归完左子树，self.head 正好指向中点
            node = TreeNode(self.head.val)
            node.left = left_child
            
            # 关键：处理完一个节点，指针向后移动一位
            self.head = self.head.next
            
            # 【右】再递归构建右子树
            node.right = convert(mid + 1, right)
            
            return node
            
        return convert(0, size - 1)